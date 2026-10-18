# schemas for response and request models

from typing import Annotated
from datetime import date
from enum import Enum
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, EmailStr, Field

# Lotto Schemas
class LottoBase(BaseModel):
    game_name: str = Field(min_length=1)
    combination: str = Field(min_length=1)
    draw_date: date
    prize_pool: Decimal = Field(gt=0, decimal_places=2)
    amount_of_winners: int | None = Field(default=None)

class LottoCreate(LottoBase):
    pass

class LottoResponse(LottoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
