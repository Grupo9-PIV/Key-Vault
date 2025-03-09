from http import HTTPStatus

from fastapi import APIRouter

from src.schemas import (
    RenewalRequestCreate,
    RenewalRequestList,
    RenewalRequestPublic,
    RenewalRequestUpdate,
)
from src.services import RenewalRequestService
from src.types import (
    T_CurrentUser,
    T_PaginationParams,
    T_RenewalRequestFilters,
    T_Session,
)

router = APIRouter(prefix='/renewal-requests', tags=['Renewal Requests'])


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=RenewalRequestPublic,
)
def create_renewal_request(
    request_data: RenewalRequestCreate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return RenewalRequestService.create_renewal_request(
        session, request_data, current_user
    )


@router.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=RenewalRequestList,
)
def read_renewal_requests(
    session: T_Session,
    current_user: T_CurrentUser,
    pagination: T_PaginationParams,
    filters: T_RenewalRequestFilters | None = None,
):
    return {
        'requests': RenewalRequestService.get_renewal_requests(
            session=session,
            pagination=pagination,
            filters=filters,
        )
    }


@router.get(
    '/{request_id}',
    status_code=HTTPStatus.OK,
    response_model=RenewalRequestPublic,
)
def read_renewal_request(
    request_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return RenewalRequestService.get_renewal_request(
        session, request_id, current_user
    )


@router.put(
    '/{request_id}',
    status_code=HTTPStatus.OK,
    response_model=RenewalRequestPublic,
)
def update_renewal_request(
    request_id: int,
    request_data: RenewalRequestUpdate,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return RenewalRequestService.update_renewal_request(
        session, request_id, request_data, current_user
    )


@router.delete(
    '/{request_id}',
    status_code=HTTPStatus.OK,
    response_model=RenewalRequestPublic,
)
def delete_renewal_request(
    request_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return RenewalRequestService.delete_renewal_request(
        session, request_id, current_user
    )


@router.post(
    '/{request_id}/approve',
    status_code=HTTPStatus.OK,
    response_model=RenewalRequestPublic,
)
def approve_renewal_request(
    session: T_Session,
    current_user: T_CurrentUser,
    request_id: int,
    feedback: str | None = None,
):
    return RenewalRequestService.approve_request(
        session, request_id, current_user, feedback
    )


@router.post(
    '/{request_id}/reject',
    status_code=HTTPStatus.OK,
    response_model=RenewalRequestPublic,
)
def reject_renewal_request(
    request_id: int,
    feedback: str,
    session: T_Session,
    current_user: T_CurrentUser,
):
    return RenewalRequestService.reject_request(
        session, request_id, current_user, feedback
    )
