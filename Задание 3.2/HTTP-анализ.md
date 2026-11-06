# Задание 3.2. Анализ HTTP через DevTools

1. Запустить Flask локально, войти на `/login` через Chrome или Edge.
2. F12 → Network → Preserve log → выполнить авторизацию тестовыми данными.
3. Выбрать `POST /login` → Headers: URL, Method, Status, Content-Type, Set-Cookie, CSP.
4. Payload: указать названия полей `login`, `password`, `csrf_token`, **не вставлять пароль и токен в отчёт**.
5. Response: после успешного входа обычно происходит HTTP 302 Redirect на `/requests` либо `/admin/`.
6. Отдельно открыть `/events/999999` и проверить ответ HTTP 404.

| Свойство | Что внести по фактическому запросу |
|---|---|
| URL | http://127.0.0.1:5000/login |
| HTTP-метод | POST |
| Status | заполнить по снимку Network |
| Content-Type запроса | заполнить по Headers |
| Ответ и Location | заполнить по Headers |
| Cookies | HttpOnly и SameSite=Lax (проверить) |
| Headers защиты | X-Frame-Options, CSP и др. (проверить) |

**Скриншоты:** `screenshots/3.2_devtools/01_headers.png`, `02_payload_redacted.png`, `03_response.png`, `04_404.png`. Не записывать секреты в HAR.

## Фактические данные, полученные в Edge DevTools

| Показатель | Результат |
|---|---|
| POST /login | 302 Found, Location: /requests |
| GET /login | 200 OK |
| GET /requests | HTML-страница загружена после авторизации |
| Тело POST | csrf_token, login, password (значения скрыты) |
| Cookie | session, HttpOnly, SameSite=Lax; Secure не установлен на локальном HTTP |
| Ответ | text/html; charset=utf-8, Cache-Control: no-store |
| Защита | CSP, X-Frame-Options: DENY, X-Content-Type-Options: nosniff |

Снимки: [Headers](../screenshots/3.2_devtools/01_post_login_headers_safe.png), [Payload](../screenshots/3.2_devtools/02_post_login_payload_safe.png), [Cookies](../screenshots/3.2_devtools/03_post_login_cookie_safe.png), [HTML Response](../screenshots/3.2_devtools/04_get_requests_html_safe.png).

## Фактические данные, полученные в Edge DevTools

| Показатель | Результат |
|---|---|
| POST /login | 302 Found, Location: /requests |
| GET /login | 200 OK |
| GET /requests | HTML-страница загружена после авторизации |
| Тело POST | csrf_token, login, password (значения скрыты) |
| Cookie | session, HttpOnly, SameSite=Lax; Secure не установлен на локальном HTTP |
| Ответ | text/html; charset=utf-8, Cache-Control: no-store |
| Защита | CSP, X-Frame-Options: DENY, X-Content-Type-Options: nosniff |

Снимки: [Headers](../screenshots/3.2_devtools/01_post_login_headers_safe.png), [Payload](../screenshots/3.2_devtools/02_post_login_payload_safe.png), [Cookies](../screenshots/3.2_devtools/03_post_login_cookie_safe.png), [HTML Response](../screenshots/3.2_devtools/04_get_requests_html_safe.png).
