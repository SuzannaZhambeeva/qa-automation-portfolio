# QA Automation Portfolio

Автотесты на Python: API, UI (Selenium) и UI (Playwright).

## Стек
Python, pytest, requests, jsonschema, Selenium, Playwright, Page Object Model

## Структура
- `api_project/` — API-тесты (CRUD, авторизация, негативные кейсы, схемы)
- `ui_tests/selenium_project/` — UI-тесты на Selenium + POM
- `ui_tests/playwright_tests/` — те же сценарии на Playwright + POM

## Запуск

1. Установить зависимости:
```bash
pip install -r requirements.txt
playwright install chromium
```

2. Задать API-ключ (нужен только для API-тестов, получить на app.reqres.in/api-keys):
```bash
export REQRES_API_KEY="ваш_ключ"
```

3. Запустить тесты. Каждый проект запускается из своей папки:

API-тесты (из корня репозитория):
```bash
pytest api_project/ -v
```

Selenium (из папки `ui_tests`):
```bash
cd ui_tests
pytest selenium_project/ -v
```

Playwright (из папки `ui_tests/playwright_tests`):
```bash
cd ui_tests/playwright_tests
pytest playwright_project/ -v
```