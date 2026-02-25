from datetime import date
from typing import List

from sqlalchemy import String, ForeignKey, UniqueConstraint, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.audit import AuditModel


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(primary_key=True)
    organization_name: Mapped[str] = mapped_column(String)
    full_name: Mapped[str | None] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    phone: Mapped[str | None] = mapped_column(String, unique=True)
    address: Mapped[str | None] = mapped_column(String)

    users: Mapped[List["User"]] = relationship(
        secondary="user_tenants",
        back_populates="tenants"
    )

    teams: Mapped[List["Team"]] = relationship(
        back_populates="tenant",
        cascade="all, delete-orphan"
    )

    owners: Mapped[List["Owner"]] = relationship(
        back_populates="tenant",
        cascade="all, delete-orphan"
    )

    players: Mapped[List["Player"]] = relationship(
        back_populates="tenant",
        cascade="all, delete-orphan"
    )

    settings: Mapped["TenantSettings | None"] = relationship(
        back_populates="tenant",
        uselist=False,
        cascade="all, delete-orphan"
    )


class TenantSettings(Base, AuditModel):
    __tablename__ = "tenant_settings"

    id: Mapped[int] = mapped_column(primary_key=True)

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"),
        unique=True
    )

    event_name: Mapped[str] = mapped_column(String)
    logo: Mapped[str | None] = mapped_column(String)
    total_overs: Mapped[int | None]
    players_per_team: Mapped[int | None]
    base_price: Mapped[float | None]
    purse_limit: Mapped[float | None]
    auction_start_date: Mapped[date | None] = mapped_column(Date)
    auction_end_date: Mapped[date | None] = mapped_column(Date)

    tenant: Mapped["Tenant"] = relationship(back_populates="settings")

    __table_args__ = (
        UniqueConstraint("tenant_id", "event_name", name="uq_tenant_event_name"),
    )
