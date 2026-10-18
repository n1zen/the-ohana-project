# models for database tables

from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

# Lotto Models
class Lotto(Base):
    __tablename__ = "lottos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    game_name: Mapped[str] = mapped_column(String(255), nullable=False)
    combination: Mapped[str] = mapped_column(String(255), nullable=False)
    draw_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    prize_pool: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=2), nullable=False)
    amount_of_winners: Mapped[int | None] = mapped_column(Integer, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))