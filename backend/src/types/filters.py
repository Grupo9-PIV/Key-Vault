from typing import Annotated

from fastapi import Depends, Query

from src.schemas import RenewalRequestFilters


# Paginação
def get_pagination_params(
    skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)
) -> dict[str, int]:
    return {'skip': skip, 'limit': limit}


T_PaginationParams = Annotated[dict[str, int], Depends(get_pagination_params)]

# Requisição de Renovação
T_RenewalRequestFilters = Annotated[RenewalRequestFilters, Depends()]
