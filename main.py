import flask
import requests
from flask import Flask, jsonify, redirect, render_template
from flask_login import current_user
from flask_restful import abort
from requests import get
import sys
from pprint import pprint
from data import db_session, users_api, jobs_api
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from flask import make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("base.html")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def map_image(name):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={name}&format=json"

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['Point']['pos']
        # Печатаем извлечённые из ответа поля:
        toponym = ','.join(toponym.split(' '))
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")

    map_request = f"https://static-maps.yandex.ru/1.x/?ll={toponym}&spn=5,5&l=map"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "static/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    from PIL import Image
    img_PIL = Image.open('static\map.png').convert('RGB')
    img_PIL.save('static\map.jpg')


@app.route('/users_show/<int:user_id>', methods=['GET'])
def users_show(user_id):
    res = get('http://localhost:5000/api/users/1').json()
    name, surname = res['users']['name'], res['users']['surname']
    city = res['users']['city_from']
    map_image(city)
    return render_template('users_show.html', name=name, surname=surname, city=city,
                           title='Миссия Колонизация Марса')


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return render_template('choiceplanet.html', planet_name=planet_name,
                           title='Миссия Колонизация Марса')


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
