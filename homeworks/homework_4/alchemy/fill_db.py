from homeworks.homework_4.alchemy import engine
from homeworks.homework_4.alchemy.connector import DBConnector
from homeworks.homework_4.alchemy.models import Category, Product

categories = [
    {'id': 1, 'name': 'Электроника', 'description': 'Гаджеты и устройства.'},
    {'id': 2, 'name': 'Книги', 'description': 'Печатные книги и электронные книги.'},
    {'id': 3, 'name': 'Одежда', 'description': 'Одежда для мужчин и женщин.'}
]

products = [
    {'id': 1, 'name': "Смартфон", 'price': 299.99, 'in_stock': True, 'category_id': 1},
    {'id': 2, 'name': "Ноутбук", 'price': 499.99, 'in_stock': True, 'category_id': 1},
    {'id': 3, 'name': "Научно-фантастический роман", 'price': 15.99, 'in_stock': True, 'category_id': 2},
    {'id': 4, 'name': "Джинсы", 'price': 40.50, 'in_stock': True, 'category_id': 3},
]

with DBConnector(engine) as session:
    for obj in categories:
        session.add(Category(**obj))
    for obj in products:
        session.add(Product(**obj))

    session.commit()
