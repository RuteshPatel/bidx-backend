from typing import List

from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.audit import AuditModel


class Team(Base, AuditModel):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE")
    )

    owner_id: Mapped[int | None] = mapped_column(
        ForeignKey("owners.id", ondelete="SET NULL")
    )

    name: Mapped[str] = mapped_column(String)
    short_name: Mapped[str | None] = mapped_column(String)
    logo: Mapped[str | None] = mapped_column(String)
    purse_amount: Mapped[float] = mapped_column(Float, default=0)

    # Relationships
    tenant: Mapped["Tenant"] = relationship(back_populates="teams")

    owner: Mapped["Owner | None"] = relationship(back_populates="teams")

    players: Mapped[List["Player"]] = relationship(
        back_populates="team",
        cascade="all"
    )
