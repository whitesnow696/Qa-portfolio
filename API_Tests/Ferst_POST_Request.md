# Отчет об API-тестировании: POST-запрос

**Цель:** Проверить, что метод POST создает новый ресурс.

**Метод:** `POST`
**URL:** `https://jsonplaceholder.typicode.com/posts`

**Тело запроса (JSON):**
```json
{
  "title": "Мой первый тестовый пост",
  "body": "Создан через Postman для портфолио",
  "userId": 1
}
