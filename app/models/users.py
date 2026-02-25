from typing import List

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.audit import AuditModel


class User(Base, AuditModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String, unique=True)
    full_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    phone: Mapped[str | None] = mapped_column(String, unique=True)
    gender: Mapped[str | None] = mapped_column(String)
    dob: Mapped[Date | None] = mapped_column(Date)
    profile_photo: Mapped[str | None] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    # Relationships
    role: Mapped["Role"] = relationship(back_populates="users")

    tenants: Mapped[List["Tenant"]] = relationship(
        secondary="user_tenants",
        back_populates="users"
    )

    owner_profile: Mapped["Owner | None"] = relationship(
        back_populates="user",
        uselist=False,
        foreign_keys="Owner.user_id",
        cascade="all, delete-orphan"
    )

    player_profile: Mapped["Player | None"] = relationship(
        back_populates="user",
        uselist=False,
        foreign_keys="Player.user_id",
        cascade="all, delete-orphan"
    )

    sessions: Mapped[List["UserSession"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )


class UserTenant(Base):
    __tablename__ = "user_tenants"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"),
        primary_key=True
    )
