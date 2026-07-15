import requests

# 1. GET-запрос (проверяем существующий пост)
url_get = "https://jsonplaceholder.typicode.com/posts/1"
response_get = requests.get(url_get)

# Проверки для GET
assert response_get.status_code == 200, f"Ошибка: статус {response_get.status_code}"
data = response_get.json()
assert data['id'] == 1, "ID поста не совпадает"
assert 'title' in data, "В ответе нет поля title"
assert 'body' in data, "В ответе нет поля body"

print("✅ GET-тест пройден! Статус 200, все поля на месте.")

# 2. POST-запрос (создаем новый пост)
url_post = "https://jsonplaceholder.typicode.com/posts"
new_post = {
    "title": "Мой автотест",
    "body": "Этот пост создан скриптом на Python",
    "userId": 1
}
response_post = requests.post(url_post, json=new_post)

# Проверки для POST
assert response_post.status_code == 201, f"Ошибка: статус {response_post.status_code}"
post_data = response_post.json()
assert post_data['id'] is not None, "ID не был создан"
assert post_data['title'] == new_post['title'], "Заголовок не совпадает"

print("✅ POST-тест пройден! Новый пост создан с ID:", post_data['id'])

print("\n🎉 Все тесты успешно выполнены!")