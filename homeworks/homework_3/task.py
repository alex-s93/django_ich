from sqlalchemy import create_engine
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Numeric
)
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('mysql+pymysql://root:<<password>>@localhost:3306/test_sqlalchemy')
Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()


class Product(Base):
    __tablename__ = 'hw_3_products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(7, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('hw_3_categories.id'))


class Category(Base):
    __tablename__ = "hw_3_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))


Base.metadata.create_all(engine)
