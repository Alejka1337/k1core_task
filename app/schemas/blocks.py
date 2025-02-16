from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from typing_extensions import Any, Self


class ProviderEnum(str, Enum):
    block_chair = "Blockchair"
    coin_market_cap = "CoinMarketCap"

class CurrencyEnum(str, Enum):
    btc = "BTC"
    eth = "ETH"


class BlockFilters(BaseModel):
    currency: Optional[CurrencyEnum] = None
    provider: Optional[ProviderEnum] = None
    limit: Optional[int] = None
    offset: Optional[int] = None


class BlockByUUID(BaseModel):
    block_id: UUID


class BlockByNumber(BaseModel):
    block_number: int


class BlockResponse(BaseModel):
    id: UUID
    currency: str
    provider: str
    block_number: int
    stored_at: str

    @classmethod
    def from_orm(cls, obj: Any) -> Self:
        return cls(
            id=obj.id,
            currency=obj.currency.name,
            provider=obj.provider.name,
            block_number=obj.block_number,
            stored_at=obj.stored_at.strftime("%H:%M:%S %m-%d-%Y")
        )
