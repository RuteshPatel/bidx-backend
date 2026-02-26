from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.middleware.auth_middleware import get_current_user
from app.permissions.custom_permission import require_super_admin
from app.schemas.admin.tenant import TenantCreate
from app.services.admin.tenant import TenantService

router = APIRouter(prefix="/tenants", tags=["Admin - Tenants"])
tenant_service_obj = TenantService()

@router.post("/", dependencies=[Depends(require_super_admin)])
def create_tenant(payload: TenantCreate, db: Session = Depends(get_db)):
    return tenant_service_obj.create_tenant(db, payload)
