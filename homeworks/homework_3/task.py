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

# Задача 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.
engine = create_engine('mysql+pymysql://root:<<password>>@localhost:3306/test_sqlalchemy')

# Задача 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# Задача 3: Определите модель продукта Product со следующими типами колонок:
#     id: числовой идентификатор
#     name: строка (макс. 100 символов)
#     price: числовое значение с фиксированной точностью
#     in_stock: логическое значение
class Product(Base):
    __tablename__ = 'hw_3_products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(7, 2))
    in_stock = Column(Boolean)

    #Задача 5: Установите связь между таблицами Product и Category с помощью колонки category_id.
    category_id = Column(Integer, ForeignKey('hw_3_categories.id'))


# Задача 4: Определите связанную модель категории Category со следующими типами колонок:
#     id: числовой идентификатор
#     name: строка (макс. 100 символов)
#     description: строка (макс. 255 символов)
class Category(Base):
    __tablename__ = "hw_3_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))


Base.metadata.create_all(engine)
