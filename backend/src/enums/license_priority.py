from enum import Enum


class LicensePriority(str, Enum):
    CRITICA = 'crítica'
    ALTA = 'alta'
    MEDIA = 'média'
    BAIXA = 'baixa'

    def __str__(self):
        return self.value
