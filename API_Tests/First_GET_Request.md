# Отчет об API-тестировании: GET-запрос

**Цель:** Проверить, что метод GET возвращает корректные данные существующего поста.

**Метод:** `GET`
**URL:** `https://jsonplaceholder.typicode.com/posts/1`

### Результат
*   **Статус-код:** `200 OK`
*   **Время ответа:** `804` мс

### Тело ответа (JSON)
```json
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere...",
    "body": "quia et suscipit..."
}
