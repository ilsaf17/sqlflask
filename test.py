from requests import get, post, delete

print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs').json())

# print(get('http://localhost:5000/api/users/show/1').json())
# print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/10').json())
# print(get('http://localhost:5000/api/jobs/sdsdwsd').json())
# print(get('http://localhost:5000/api/users').json())
#

# print(delete('http://localhost:5000/api/users/3').json())
#
# print(post('http://localhost:5000/api/users',
#            json={'id': 4,
#                'name': 'Заголовок112',
#                'position': 'Текст н2овости1122',
#                'email': 'dfdf111222',
#            }).json())



# print(post('http://localhost:5000/api/jobs',
#            json={'team_leader': 1,
#                  'job': 'Текст новости111',
#                  'work_size': 1
#                  }).json())