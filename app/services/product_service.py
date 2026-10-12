from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductPatch, ProductResponse, ProductUpdate

class ProductService:
    def __init__(self, db: AsyncSession):
        self.repository = ProductRepository(db)

    async def create_product(self, product_in: ProductCreate) -> ProductResponse:
        existing_sku = await self.repository.get_by_sku(product_in.sku)
        if existing_sku:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with SKU '{product_in.sku}' already exists."
            )
        return await self.repository.create(product_in)

    async def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = await self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} not found."
            )
        return product

    async def list_products(self, skip: int = 0, limit: int = 10, name: Optional[str] = None) -> List[ProductResponse]:
        return await self.repository.get_all(skip=skip, limit=limit, name=name)

    async def update_product(self, product_id: int, product_in: ProductUpdate) -> ProductResponse:
        db_product = await self.repository.get_by_id(product_id)
        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} not found."
            )

        if db_product.sku != product_in.sku:
            sku_check = await self.repository.get_by_sku(product_in.sku)
            if sku_check:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Product with SKU '{product_in.sku}' already exists."
                )

        return await self.repository.update(db_product, product_in)

    async def patch_product(self, product_id: int, product_in: ProductPatch) -> ProductResponse:
        db_product = await self.repository.get_by_id(product_id)
        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} not found."
            )

        if product_in.sku is not None and product_in.sku != db_product.sku:
            sku_check = await self.repository.get_by_sku(product_in.sku)
            if sku_check:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Product with SKU '{product_in.sku}' already exists."
                )

        return await self.repository.patch(db_product, product_in)

    async def delete_product(self, product_id: int) -> None:
        db_product = await self.repository.get_by_id(product_id)
        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} not found."
            )
        await self.repository.delete(db_product)