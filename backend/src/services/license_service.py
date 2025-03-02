import re  # precisa para validar as chaves das licenças
from sqlalchemy.orm import Session
from src.models.license import License
from src.schemas.license import LicenseCreate, LicenseUpdate
from src.exceptions import (
    LicenseNotFoundException,
    LicenseExpiredException,
    LicensePendingException,
    LicenseDeactivatedException,
    LicenseInvalidException,
)
from typing import (
    Union,
)  # essa função declara que uma variável pode ter vários tipos de dados
from src.models.license import LicenseType
from datetime import datetime
from fastapi import Response


# criação do método estático pra chamar todas as funções pela classe LicenseService
class LicenseService:
    # regras para cada software, para cada nome de software, adicionar uma quant alfanum de caracteres
    SOFTWARE_LICENSE_RULES = {
        'windows': 25,
        'adobe': 24,
        'office': 20,
    }

    @staticmethod
    def validate_license_type(
        license_type: Union[str, LicenseType, None],
    ) -> Union[str, None]:
        """
        Valida e mapeia o tipo de licença.
        - Se for uma assinatura, aceita valores como "Anual", "Mensal" ou "Trimestral".
        - Se for freemium, aceita valores personalizados (se necessário).
        - Caso contrário, valida se o valor é um LicenseType válido.
        """
        if license_type is None:
            return None  # Aceita valores nullable

        if isinstance(license_type, LicenseType):
            return license_type.value  # Retorna o valor do enum como string

        # Converte para minúsculas para facilitar a comparação e garante que tudo seja str na entrada
        license_type_lower = str(license_type).lower()

        # Verifica se o valor é válido
        valid_types = ['anual', 'mensal', 'trimestral', 'freemium']
        if license_type_lower in valid_types:
            return license_type  # Retorna o valor original

        # Verifica se o valor é um LicenseType válido
        try:
            return LicenseType(
                license_type_lower
            ).value  # Retorna o valor do enum como string
        except ValueError:
            raise ValueError(f'Tipo de licença inválido: {license_type}')

    @staticmethod
    def normalize_license_type(license_type: str) -> str:
        if license_type in ['anual', 'mensal', 'trimestral']:
            return 'assinatura'
        return license_type

    @staticmethod
    # Função para criar uma nova licença
    def create_license(db: Session, license_data: LicenseCreate):
        # Criação da nova licença

        # Converte o objeto Pydantic em um dicionário ou JSON
        validated_data = license_data.model_dump()

        # Valida e mapeia o tipo de licença
        validated_data['license_type'] = LicenseService.validate_license_type(
            validated_data.get('license_type')
        )

        # Normaliza o nome do software para minúsculas
        software_name = validated_data['software_name'].lower()
        validated_data['software_name'] = software_name

        # Se o software estiver na lista de regras, valida a chave
        if software_name in LicenseService.SOFTWARE_LICENSE_RULES:
            license_key = validated_data.get('license_key', '')
            expected_length = LicenseService.SOFTWARE_LICENSE_RULES[
                software_name
            ]

            # Regex para verificar se a chave é alfanumérica e tem o tamanho esperado
            if not re.fullmatch(
                r'^[A-Za-z0-9]{' + str(expected_length) + r'}$', license_key
            ):
                raise ValueError(
                    f'A chave de licença para {software_name.capitalize()} deve conter exatamente {expected_length} caracteres alfanuméricos.'
                )

        new_license = License(
            **validated_data
        )  # desempacota o dicionário em argumentos
        db.add(new_license)
        db.commit()
        db.refresh(new_license)
        return new_license

    @staticmethod
    # Função para buscar uma licença por ID
    def get_license(db: Session, license_id: int):
        license_obj = (
            db.query(License).filter(License.id == license_id).first()
        )
        if not license_obj:
            raise LicenseNotFoundException()
        return license_obj

    @staticmethod
    # Função para buscar todas as licenças
    def get_all_licenses(db: Session, skip: int = 0, limit: int = 10):
        return db.query(License).offset(skip).limit(limit).all()

    @staticmethod
    # Função para atualizar uma licença
    def update_license(
        db: Session, license_id: int, license_data: LicenseUpdate
    ):
        # descobre se é um objeto licença pela id dela
        license_obj = (
            db.query(License).filter(License.id == license_id).first()
        )
        if not license_obj:
            raise LicenseNotFoundException()

        # Converte o objeto Pydantic em um dicionário ou JSON
        validated_data = license_data.model_dump(exclude_unset=True)

        # Valida e mapeia o tipo de licença
        if 'license_type' in validated_data:
            validated_data['license_type'] = (
                LicenseService.validate_license_type(
                    validated_data['license_type']
                )
            )

        # Valida a nova license_key (se for fornecida)
        if 'license_key' in validated_data:
            software_name = license_obj.software_name.lower()
            if software_name in LicenseService.SOFTWARE_LICENSE_RULES:
                license_key = validated_data['license_key']
                expected_length = LicenseService.SOFTWARE_LICENSE_RULES[
                    software_name
                ]

                # Regex para validar a nova chave
                if not re.fullmatch(
                    r'^[A-Za-z0-9]{' + str(expected_length) + r'}$',
                    license_key,
                ):
                    raise ValueError(
                        f'A chave de licença para {software_name.capitalize()} deve conter exatamente {expected_length} caracteres alfanuméricos.'
                    )

        # Lista de campos obrigatórios
        required_fields = [
            'software_name',
            'license_type',
            'status',
            'developed_by',
            'start_date',
            'end_date',
            'purchase_date',
            'license_key',
        ]

        # Mantém os valores existentes para campos obrigatórios não fornecidos
        for field in required_fields:
            if field not in validated_data:
                validated_data[field] = getattr(license_obj, field)

        for field, value in validated_data.items():
            setattr(license_obj, field, value)

        db.commit()
        db.refresh(license_obj)
        return license_obj

    @staticmethod
    # Função para deletar uma licença
    def delete_license(db: Session, license_id: int):
        license_obj = (
            db.query(License).filter(License.id == license_id).first()
        )
        if not license_obj:
            raise LicenseNotFoundException()

        db.delete(license_obj)
        db.commit()
        return Response(status_code=204)

    # passei as verificações do arquivo que estava em security para cá.
    @staticmethod
    def verify_license_key(db: Session, license_key: str):
        """
        Função para verificar a chave de licença.
        Valida se a licença existe e se está em um estado válido (ativa).
        """
        license = (
            db.query(License)
            .filter(License.license_key == license_key)
            .first()
        )

        if not license:
            raise LicenseNotFoundException()

        if license.end_date < datetime.now():
            raise LicenseExpiredException()

        if license.status == LicenseStatus.PENDENTE:
            raise LicensePendingException()

        if license.status == LicenseStatus.DESATIVADA:
            raise LicenseDeactivatedException()

        if license.status == LicenseStatus.INVALIDA:
            raise LicenseInvalidException()

        return license
