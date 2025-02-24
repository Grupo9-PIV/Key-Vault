from enum import Enum


class LicenseType(str, Enum):
    ASSINATURA = 'assinatura'
    PERPETUA = 'perpétua'
    TRIAL = 'trial'
    EDUCACIONAL = 'educacional'
    CORPORATIVA = 'corporativa'
    OPEN_SOURCE = 'open_source'
    FREEMIUM = 'freemium'
    PAY_PER_USE = 'pay_per_use'

    def __str__(self):   # pragma: no cover
        return self.value
