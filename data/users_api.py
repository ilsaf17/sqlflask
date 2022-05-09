import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'position', 'email'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_user(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'users': users.to_dict(only=(
                'id', 'position', 'email', 'city_from', 'name', 'surname'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'position', 'email']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    users = User(
        name=request.json['name'],
        position=request.json['position'],
        email=request.json['email'],
    )
    db_sess.add(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users', methods=['POST'])
def edit_user(id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name', 'position', 'email']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(request.json['id'])
    if not users:
        return jsonify({'error': 'Not found'})
    db_sess.delete(users)
    db_sess.commit()
    db_sess = db_session.create_session()
    user = User(
        id=request.json['id'],
        name=request.json['name'],
        position=request.json['position'],
        email=request.json['email'],
    )
    db_sess.add(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(id)
    if not users:
        return jsonify({'error': 'Not found'})
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})
