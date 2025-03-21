from typing import Optional

from pydantic import BaseModel

from src.enums import RequestStatus


class RenewalRequestCreate(BaseModel):
    license_id: int
    reason: Optional[str] = None


class RenewalRequestUpdate(BaseModel):
    manager_id: Optional[int] = None
    reason: Optional[str] = None


class RenewalRequestPublic(BaseModel):
    id: int
    license_id: int
    requested_by_id: int
    manager_id: int
    reason: str
    feedback: str
    status: RequestStatus

    class Config:
        from_attributes = True


class RenewalRequestList(BaseModel):
    requests: list[RenewalRequestPublic]


class RenewalRequestFilters(BaseModel):
    requested_by: Optional[int] = None
    managed_by: Optional[int] = None
    license_name: Optional[str] = None

    class Config:
        extra = 'forbid'
