from requests import get, post, delete

print(get('http://localhost:5000/api/users').json())

print(get('http://localhost:5000/api/users/2').json())

print(post('http://localhost:5000/api/users',
           json={'name': 'Заголовок111',
                 'position': 'Текст новости111',
                 'email': 'dfdf111',
                 }).json())


print(delete('http://localhost:5000/api/users/3').json())

print(post('http://localhost:5000/api/users',
           json={'id': 4,
               'name': 'Заголовок112',
               'position': 'Текст н2овости1122',
               'email': 'dfdf111222',
           }).json())
