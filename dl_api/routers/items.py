from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/items",
    tags=["items"],
)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Get method with Query params


# @router.get("/{item_id}")
# async def read_item(item_id: int, q: list[str]  None = Query(None, title="Query", description="Query description", deprecated=True)):
#     return {"item_id": item_id, "q": q}

# Put method with Body params


@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
