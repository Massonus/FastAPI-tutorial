from typing import Annotated
from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest/")
def latest():
    return {
        "item": {
            "item_id": 1,
            "item_name": "Item1"
        }
    }


@router.get("/{item_id}/")
def item_id(item_id: Annotated[int, Path(ge=1, lt=1000000)]):
    return {"item_id": item_id}