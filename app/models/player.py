from sqlalchemy import ForeignKey, Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.audit import AuditModel


class Player(Base, AuditModel):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE")
    )

    team_id: Mapped[int | None] = mapped_column(
        ForeignKey("teams.id", ondelete="SET NULL")
    )

    playing_role: Mapped[str | None] = mapped_column(String)
    batting_style: Mapped[str | None] = mapped_column(String)
    bowling_style: Mapped[str | None] = mapped_column(String)
    base_price: Mapped[float | None] = mapped_column(Float)

    # Relationships
    user: Mapped["User"] = relationship(
        foreign_keys=[user_id],
        back_populates="player_profile"
    )

    tenant: Mapped["Tenant"] = relationship(back_populates="players")

    team: Mapped["Team | None"] = relationship(back_populates="players")
