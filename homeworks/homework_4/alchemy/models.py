from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from homeworks.homework_4.alchemy import Base, engine


class Category(Base):
    __tablename__ = "hw4_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "hw4_products"
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("hw4_categories.id"))
    name = Column(String(50))
    price = Column(Numeric(7, 2))
    in_stock = Column(Boolean)

    category = relationship('Category', back_populates="products")


Base.metadata.create_all(engine)

