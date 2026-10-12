from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductPatch, ProductUpdate

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        query = select(Product).where(Product.id == product_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_by_sku(self, sku: str) -> Optional[Product]:
        query = select(Product).where(Product.sku == sku)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10, name: Optional[str] = None) -> List[Product]:
        query = select(Product)
        if name:
            query = query.where(Product.name.icontains(name))
        query = query.offset(skip).limit(limit)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def create(self, product_in: ProductCreate) -> Product:
        db_product = Product(**product_in.model_dump())
        self.db.add(db_product)
        await self.db.commit()
        await self.db.refresh(db_product)
        return db_product

    async def update(self, db_product: Product, product_in: ProductUpdate) -> Product:
        for key, value in product_in.model_dump().items():
            setattr(db_product, key, value)
        await self.db.commit()
        await self.db.refresh(db_product)
        return db_product

    async def patch(self, db_product: Product, product_in: ProductPatch) -> Product:
        update_data = product_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
        await self.db.commit()
        await self.db.refresh(db_product)
        return db_product

    async def delete(self, db_product: Product) -> None:
        await self.db.delete(db_product)
        await self.db.commit()