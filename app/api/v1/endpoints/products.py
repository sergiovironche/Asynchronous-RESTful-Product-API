from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductPatch, ProductResponse, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(prefix="/api/v1/products", tags=["Products"])

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product_in: ProductCreate, db: AsyncSession = Depends(get_db)):
    service = ProductService(db)
    return await service.create_product(product_in)

@router.get("/", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
async def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    name: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
):
    service = ProductService(db)
    return await service.list_products(skip=skip, limit=limit, name=name)

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    service = ProductService(db)
    return await service.get_product_by_id(product_id)

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product_in: ProductUpdate, db: AsyncSession = Depends(get_db)):
    service = ProductService(db)
    return await service.update_product(product_id, product_in)

@router.patch("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def patch_product(product_id: int, product_in: ProductPatch, db: AsyncSession = Depends(get_db)):
    service = ProductService(db)
    return await service.patch_product(product_id, product_in)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    service = ProductService(db)
    await service.delete_product(product_id)
    return None