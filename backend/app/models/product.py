from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from ..database import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)

    category = relationship("Category", back_populates="products")

