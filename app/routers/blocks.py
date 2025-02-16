from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from app.dal.blocks import select_block_by_id, select_list_blocks, select_block_by_number
from app.schemas.blocks import BlockByNumber, BlockByUUID, BlockFilters, BlockResponse
from app.utils.auth import get_current_user

blocks_router = APIRouter(prefix="/blocks", tags=["Blocks"])


@blocks_router.get(
    path="/list",
    status_code=status.HTTP_200_OK,
    response_model=list[BlockResponse],
    dependencies=[Depends(get_current_user)]
)
def get_blocks_list(filters: Annotated[BlockFilters, Query()]):
    return select_list_blocks(filters=filters)


@blocks_router.get(
    path="/get/id",
    status_code=status.HTTP_200_OK,
    response_model=BlockResponse,
    dependencies=[Depends(get_current_user)]
)
def get_block_by_id(data: Annotated[BlockByUUID, Query()]):
    return select_block_by_id(block_id=data.block_id)


@blocks_router.get(
    path="/get/number",
    status_code=status.HTTP_200_OK,
    response_model=BlockResponse,
    dependencies=[Depends(get_current_user)])
def get_block_by_number(data: Annotated[BlockByNumber, Query()]):
    return select_block_by_number(block_number=data.block_number)
