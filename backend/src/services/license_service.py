import re  # precisa para validar as chaves das licenças
from datetime import datetime
from typing import (
    Any,
    Dict,
    Union,
)  # essa função declara que uma variável pode ter vários tipos de dados

from fastapi import Response
from sqlalchemy.orm import Session

from src.exceptions import (
    LicenseDeactivatedException,
    LicenseExpiredException,
    LicenseInvalidException,
    LicenseNotFoundException,
    LicensePendingException,
)
from src.models.license import License, LicenseStatus, LicenseType
from src.schemas.license import LicenseCreate, LicenseUpdate


# método estático pra chamar todas as funções pela classe LicenseService
class LicenseService:
    # nome de software, adicionar uma quant alfanum de caracteres
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
        - Converte para minúsculas antes de validar.
        - Caso contrário, valida se o valor está no enum LicenseType.
        """
        if license_type is None:
            return None  # Aceita valores nulos

        if isinstance(license_type, LicenseType):
            return license_type.value  # Retorna o valor do enum como string

        # Converte para string e minúsculas
        license_type_lower = str(license_type).strip().lower()

        # Mapeia variações de entrada para fins de validação
        valid_types = {
            'assinatura': 'assinatura',
            'freemium': 'freemium',
            'perpétua': 'perpétua',
            'corporativa': 'corporativa',
            'educacional': 'educacional',
            'open_source': 'open_source',
            'pay_per_use': 'pay_per_use',
        }

        # Verifica se o tipo de licença para fins de validação
        if license_type_lower in valid_types:
            return valid_types[license_type_lower]

        # Verifica se está no enum LicenseType
        try:
            # Tenta converter o valor para o enum LicenseType
            return LicenseType(license_type_lower).value
        except ValueError:
            # Se não for um valor válido, lança uma exceção
            raise ValueError(f'Tipo de licença inválido: {license_type}')

    @staticmethod
    def validate_license_status(
        license_status: Union[str, LicenseType, None],
    ) -> Union[str, None]:
        """
        Valida e mapeia o status de licença.
        - ativa, expirada, pendente, desativada e inválida.
        - Caso contrário, valida se o valor é um LicenseStatus válido.
        """
        if license_status is None:
            return None  # Aceita valores nullable

        if isinstance(license_status, LicenseStatus):
            return license_status.value  # Retorna o valor do enum como string

        # Converte para minúsculas e str
        license_status_lower = str(license_status).lower()

        # Verifica se o valor é válido
        valid_status = [
            'ativa',
            'expirada',
            'pendente',
            'desativada',
            'inválida',
        ]
        if license_status_lower in valid_status:
            return license_status  # Retorna o valor original

        # Verifica se o valor é um LicenseType válido
        try:
            return LicenseStatus(
                license_status_lower
            ).value  # Retorna o valor do enum como string
        except ValueError:
            raise ValueError(f'Status de licença inválido: {license_status}')

    @staticmethod
    def normalize_license_status(license_status: str) -> str:
        return license_status

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

            # Regex verifica se a chave é alfanum e tem o tamanho esperado
            if not re.fullmatch(
                r'^[A-Za-z0-9]{' + str(expected_length) + r'}$', license_key
            ):
                raise ValueError(
                    f'A chave de licença do {software_name.capitalize()} '
                    f'requer {expected_length} caracteres.'
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
    def update_license(
        db: Session, license_id: int, license_data: LicenseUpdate
    ) -> License:
        """
        Atualiza todos os campos de uma licença.
        Substitui os valores existentes pelos valores fornecidos.
        """
        license_obj = (
            db.query(License).filter(License.id == license_id).first()
        )
        if not license_obj:
            raise LicenseNotFoundException()

        # Converte o objeto Pydantic em um dicionário
        validated_data = license_data.model_dump()

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
                        f'A chave de licença do {software_name.capitalize()} '
                        f'requer {expected_length} caracteres alfanuméricos.'
                    )
                        f'A chave de licença do {software_name.capitalize()} '
                        f'requer {expected_length} caracteres alfanuméricos.'
                    )

        # Atualiza todos os campos fornecidos
        for field, value in validated_data.items():
            setattr(license_obj, field, value)

        db.commit()
        db.refresh(license_obj)
        return license_obj

    @staticmethod
    def partial_update_license(
        db: Session, license_id: int, update_data: Dict[str, Any]
    ) -> License:
        """
        Atualiza parcialmente licença.
        mantendo os valores existentes para os demais.
        """
        license_obj = (
            db.query(License).filter(License.id == license_id).first()
        )
        if not license_obj:
            raise LicenseNotFoundException()

        # Valida e mapeia o tipo de licença (se fornecido)
        if 'license_type' in update_data:
            update_data['license_type'] = LicenseService.validate_license_type(
                update_data['license_type']
            )

        # Valida a nova license_key (se for fornecida)
        if 'license_key' in update_data:
            software_name = license_obj.software_name.lower()
            if software_name in LicenseService.SOFTWARE_LICENSE_RULES:
                license_key = update_data['license_key']
                expected_length = LicenseService.SOFTWARE_LICENSE_RULES[
                    software_name
                ]

                # Regex para validar a nova chave
                if not re.fullmatch(
                    r'^[A-Za-z0-9]{' + str(expected_length) + r'}$',
                    license_key,
                ):
                    raise ValueError(
                        f'A chave de licença do {software_name.capitalize()} '
                        f'requer {expected_length} caracteres alfanuméricos.'
                    )

        # Atualiza apenas os campos fornecidos
        for field, value in update_data.items():
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

        if license.end_date and license.end_date < datetime.now():
            raise LicenseExpiredException()

        if license.status == LicenseStatus.PENDENTE:
            raise LicensePendingException()

        if license.status == LicenseStatus.DESATIVADA:
            raise LicenseDeactivatedException()

        if license.status == LicenseStatus.INVALIDA:
            raise LicenseInvalidException()

        return license
