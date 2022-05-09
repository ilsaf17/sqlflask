import flask
from flask import Flask, jsonify
from data import db_session, users_api, jobs_api
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from flask import make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(users_api.blueprint)
    app.register_blueprint(jobs_api.blueprint)

    # print(get_all_users())
    app.run()


if __name__ == '__main__':
    main()
