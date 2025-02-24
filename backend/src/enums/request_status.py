from enum import Enum


class RequestStatus(str, Enum):
    PENDENTE = 'pendente'
    APROVADA = 'aprovada'
    REJEITADA = 'rejeitada'

    def __str__(self):  # pragma: no cover
        return self.value
