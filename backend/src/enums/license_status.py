from enum import Enum


class LicenseStatus(str, Enum):
    ATIVA = 'ativa'
    EXPIRADA = 'expirada'
    PENDENTE = 'pendente'
    DESATIVADA = 'desativada'
    INVALIDA = 'inválida'

    def __str__(self):
        return self.value
