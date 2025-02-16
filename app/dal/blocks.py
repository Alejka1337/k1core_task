from uuid import UUID

from django.utils import timezone

from app.exceptions import BlockNotFoundException, CurrencyOrProviderNotFoundException
from app.models import Block, Currency, Provider
from app.schemas import BlockFilters, BlockResponse


def select_list_blocks(filters: BlockFilters) -> list[BlockResponse]:
    qs = Block.objects.all()

    if filters.currency:
        qs = qs.filter(currency__name__iexact=filters.currency)

    if filters.provider:
        qs = qs.filter(provider__name__iexact=filters.provider)

    offset = filters.offset or 0
    limit = filters.limit or 10
    qs = qs[offset: offset + limit]

    blocks = list(qs)
    return [BlockResponse.from_orm(block) for block in blocks]


def select_block_by_id(block_id: UUID) -> BlockResponse:
    try:
        block = Block.objects.get(id=block_id)
        return BlockResponse.from_orm(block)

    except Block.DoesNotExist:
        raise BlockNotFoundException()


def select_block_by_number(block_number: int) -> BlockResponse:
    try:
        block = Block.objects.get(block_number=block_number)
        return BlockResponse.from_orm(block)

    except Block.DoesNotExist:
        raise BlockNotFoundException()


def create_block(currency_name: str, provider_name: str, block_number: int):
    try:
        currency = Currency.objects.get(name=currency_name)
        provider = Provider.objects.get(name=provider_name)

    except (Currency.DoesNotExist, Provider.DoesNotExist):
        raise CurrencyOrProviderNotFoundException()

    exists_flag = Block.objects.filter(
        currency=currency,
        provider=provider,
        block_number=block_number).exists()

    if not exists_flag:
        Block.objects.create(
            currency=currency,
            provider=provider,
            block_number=block_number,
            stored_at=timezone.now()
        )

        return True
    return False
