from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(ProductUpdate):
    name: str | None = None
    description: str | None = None
    price: int | None = None


class Product(ProductBase):
    # to convert sqlalchemy objects to dict
    model_config = ConfigDict(from_attributes=True)

    id: int
