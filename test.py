from requests import get, post, delete

# TEST users_resource
# correct:
print(get('http://localhost:5000/api/users').json())
print(get('http://localhost:5000/api/users/1').json())
print(post('http://localhost:5000/api/users',
           json={'name': 'sss',
                 'position': 'Текст новости1112',
                 'email': 'ssds3'
                 }).json())
print(delete('http://localhost:5000/api/users/1').json())
# incorect:
# undefined id:
print(get('http://localhost:5000/api/users/999').json())
# hasnt defined all arguments in post
print(post('http://localhost:5000/api/users',
           json={'name': 'sss',
                 'position': 'Текст новости1112'
                 }).json())
# empty json
print(post('http://localhost:5000/api/users',
           json={}).json())
# undefined id deleting
print(delete('http://localhost:5000/api/users/999').json())





# не ввели все необходимые параметры
# print(post('http://localhost:5000/api/jobs',
#            json={'team_leader': 2,
#                  'job': 'Текст новости1112'
#                  }).json())

