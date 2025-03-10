from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import select

from src.enums import LicenseStatus, RequestStatus, UserRole
from src.exceptions import (
    LicenseNotFoundException,
    PermissionDeniedException,
    RenewalRequestNotFoundException,
)
from src.models import License, RenewalRequest, User
from src.schemas import (
    RenewalRequestCreate,
    RenewalRequestFilters,
    RenewalRequestUpdate,
)


class RenewalRequestService:
    @staticmethod
    def create_renewal_request(
        session: Session,
        request_data: RenewalRequestCreate,
        current_user: User,
    ) -> RenewalRequest:
        db_license = RenewalRequestService._get_license_or_raise(
            session, request_data.license_id
        )

        new_request = RenewalRequest(
            **request_data.model_dump(),
            requested_by_id=current_user.id,
            manager_id=db_license.manager_id,
        )

        session.add(new_request)
        session.commit()
        session.refresh(new_request)

        return new_request

    @staticmethod
    def get_renewal_requests(
        session: Session,
        pagination: dict[str, int],
        filters: RenewalRequestFilters | None = None,
    ) -> list[RenewalRequest]:
        query = select(RenewalRequest).options(
            joinedload(RenewalRequest.request_license),
            joinedload(RenewalRequest.requested_by),
        )

        if filters:
            if filters.requested_by:
                query = query.where(
                    RenewalRequest.requested_by_id == filters.requested_by
                )

            if filters.managed_by:
                query = query.where(
                    RenewalRequest.manager_id == filters.managed_by
                )

            if filters.license_name:
                query = query.join(RenewalRequest.request_license).where(
                    License.name.contains(filters.license_name.lower())
                )

        return session.scalars(
            query.offset(pagination['skip']).limit(pagination['limit'])
        ).all()

    @staticmethod
    def get_renewal_request(
        session: Session, request_id: int, current_user: User
    ) -> RenewalRequest:
        request = RenewalRequestService._get_request_or_raise(
            session, request_id
        )
        RenewalRequestService._validate_permission(request, current_user)

        return request

    @staticmethod
    def update_renewal_request(
        session: Session,
        request_id: int,
        request_data: RenewalRequestUpdate,
        current_user: User,
    ) -> RenewalRequest:
        request = RenewalRequestService._get_request_or_raise(
            session, request_id
        )
        RenewalRequestService._validate_permission(request, current_user)

        update_data = request_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(request, field, value)

        session.commit()
        session.refresh(request)

        return request

    @staticmethod
    def delete_renewal_request(
        session: Session, request_id: int, current_user: User
    ) -> RenewalRequest:
        request = RenewalRequestService._get_request_or_raise(
            session, request_id
        )
        RenewalRequestService._validate_permission(
            request, current_user, manager_ok=False
        )

        session.delete(request)
        session.commit()

        return request

    @staticmethod
    def approve_request(
        session: Session,
        request_id: int,
        current_user: User,
        feedback: str | None,
    ) -> RenewalRequest:
        request = RenewalRequestService._get_request_or_raise(
            session, request_id
        )
        db_license = RenewalRequestService._get_license_or_raise(
            session, request.license_id
        )

        RenewalRequestService._validate_permission(
            request, current_user, owner_ok=False
        )

        request.status = RequestStatus.APROVADO
        request.feedback = feedback
        db_license.status = LicenseStatus.ATIVA

        session.commit()
        session.refresh(request)

        return request

    @staticmethod
    def reject_request(
        session: Session,
        request_id: int,
        current_user: User,
        feedback: str,
    ) -> RenewalRequest:
        request = RenewalRequestService._get_request_or_raise(
            session, request_id
        )
        db_license = RenewalRequestService._get_license_or_raise(
            session, request.license_id
        )

        RenewalRequestService._validate_permission(
            request, current_user, owner_ok=False
        )

        request.status = RequestStatus.REPROVADO
        request.feedback = feedback
        db_license.status = LicenseStatus.DESATIVADA

        session.commit()
        session.refresh(request)

        return request

    # Helper functions
    @staticmethod
    def _get_request_or_raise(
        session: Session, request_id: int
    ) -> RenewalRequest:
        request = session.scalar(
            select(RenewalRequest)
            .where(RenewalRequest.id == request_id)
            .options(joinedload(RenewalRequest.request_license))
            .options(joinedload(RenewalRequest.requested_by))
        )
        if not request:
            raise RenewalRequestNotFoundException()

        return request

    @staticmethod
    def _get_license_or_raise(session: Session, license_id: int) -> License:
        db_license = session.scalar(
            select(License).where(License.id == license_id)
        )
        if not db_license:
            raise LicenseNotFoundException()

        return db_license

    @staticmethod
    def _validate_permission(
        request: RenewalRequest,
        current_user: User,
        manager_ok: bool = True,
        owner_ok: bool = True,
    ) -> None:
        is_manager_allowed = manager_ok and (
            current_user.id == request.manager_id
        )
        is_owner_allowed = owner_ok and (
            current_user.id == request.requested_by_id
        )

        if (
            current_user.role != UserRole.ADMIN
            and not is_owner_allowed
            and not is_manager_allowed
        ):
            raise PermissionDeniedException()
