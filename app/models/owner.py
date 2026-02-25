
from typing import List

from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.audit import AuditModel


class Owner(Base, AuditModel):
    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE")
    )

    wallet_balance: Mapped[float] = mapped_column(Float, default=0)

    # Relationships
    user: Mapped["User"] = relationship(
        foreign_keys=[user_id],
        back_populates="owner_profile"
    )

    tenant: Mapped["Tenant"] = relationship(back_populates="owners")

    teams: Mapped[List["Team"]] = relationship(
        back_populates="owner",
        cascade="all"
    )
