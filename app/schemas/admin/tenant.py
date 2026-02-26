from pydantic import BaseModel, EmailStr


class TenantCreate(BaseModel):
    organization_name: str
    full_name: str | None = None
    email: EmailStr
    phone: str | None = None
    address: str | None = None
