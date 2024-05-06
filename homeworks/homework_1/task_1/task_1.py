from flask import Flask

app = Flask(__name__)


# Ошибка в маршрутизаторе. Должен присутсвовать слэщ в прокидываемом аргументе, а не пустая строка
@app.route('')
def home():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
