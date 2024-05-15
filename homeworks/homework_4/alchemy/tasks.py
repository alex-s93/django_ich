from sqlalchemy import func
from homeworks.homework_4.alchemy import engine
from homeworks.homework_4.alchemy.connector import DBConnector
from homeworks.homework_4.alchemy.models import Category, Product

with DBConnector(engine) as session:
    # Извлеките все записи из таблицы categories. Для каждой категории извлеките и выведите все связанные с ней
    # продукты, включая их названия и цены.
    categories = session.query(Category).all()
    for category in categories:
        print(f"Category: {category.name}")
        print("_" * 100)
        for product in category.products:
            print(f"{product.name:<30} | {product.price}")
        print("=" * 100)

    print("*"*100)

    # Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.
    smartphone = session.query(Product).filter(Product.name == "Смартфон").one()
    if smartphone:
        print("OLD PRICE:", smartphone.price)
        smartphone.price = 349.99
        session.commit()
        print("NEW PRICE:", smartphone.price)

    print("*"*100)

    # Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.
    products_count = session.query(
        Category.name,
        func.count(Product.id).label("product_count")
    ).join(Category).group_by(Product.category_id).all()

    print("Category: Amount of products")
    print("_"*100)
    for group in products_count:
        print(f"{group.name}: {group.product_count}")

    print("*"*100)

    # Отфильтруйте и выведите только те категории, в которых более одного продукта.
    big_categories = session.query(
        Category.name, func.count(Product.id).label("product_amount")
    ).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()

    print("Categories with amount of products more that 1:")
    print("_"*100)
    for category in big_categories:
        print(f"{category.name}")