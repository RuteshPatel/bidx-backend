from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Tenant
from app.repository.base import BaseRepository
from app.schemas.admin.tenant import TenantCreate


class TenantService:
    def create_tenant(self, db: Session, payload: TenantCreate):
        base_repo = BaseRepository(db, Tenant)

        existing = db.query(Tenant).filter(
            Tenant.email == payload.email
        ).first()

        if existing:
            raise HTTPException(status_code=400, detail="Tenant already exists")

        tenant = Tenant(**payload.model_dump())

        db.add(tenant)
        db.commit()
        db.refresh(tenant)

        return tenant
