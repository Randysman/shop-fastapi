from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=4, max_length=25, description="Category name")
    slug: str = Field(..., min_length=4, max_length=25, description="Slug")


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Category ID")

    class Config:
        from_attributes = True