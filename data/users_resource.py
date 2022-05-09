from data.jobs import Jobs
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from args_parser import parser
from data import db_session
from data.users import User


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(Jobs).get(users_id)
    if not users:
        abort(404, message=f"users {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({'users': users.to_dict(
            only=('surname', 'name', 'age',
                  'position', 'speciality', 'address', 'email'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age',
                  'position', 'speciality', 'address', 'email'))
            for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
