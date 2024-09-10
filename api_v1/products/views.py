from sys import prefix

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import product_by_id
from core.models import db_helper
from .schemas import Product, ProductCreate, ProductUpdate

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product_in=product)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
    product=Depends(product_by_id),
):
    return product


@router.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product=Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )
