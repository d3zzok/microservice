# Микросервисная архитектура интернет-магазина

Проект представляет собой микросервисную архитектуру для интернет-магазина электроники, разработанную на Python с использованием FastAPI и Docker.

Архитектура проекта

Проект состоит из трех независимых микросервисов:

🛍️ Order Service (Сервис заказов)
- Порт: 8001
- Назначение: Управление пользователями, корзинами и заказами
- База данных: PostgreSQL (orderdb)
- Основные функции:
  - Регистрация и управление пользователями
  - Работа с корзиной покупок
  - Создание и отслеживание заказов
  - Координация с другими сервисами

💳 Payment Service (Сервис платежей)
- Порт: 8002
- Назначение: Обработка платежных транзакций
- База данных: PostgreSQL (paymentdb)
- Основные функции:
  - Обработка платежей
  - Управление статусами транзакций
  - История платежей

### 🚚 Delivery Service (Сервис доставки)
- Порт: 8003
- Назначение: Управление доставкой заказов
- База данных: PostgreSQL (deliverydb)
- Основные функции:
  - Создание записей о доставке
  - Отслеживание статусов доставки
  - Генерация трек-номеров

## Технологический стек

- Backend: Python 3.9, FastAPI
- Базы данных: PostgreSQL
- Контейнеризация: Docker, Docker Compose
- ORM: SQLAlchemy
- Миграции: Alembic (может быть добавлен)

Структура проекта
microservices-shop/
├── docker-compose.yml
├── order-service/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── routers/
├── payment-service/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app/
│ ├── main.py
│ ├── database.py
│ └── models.py
└── delivery-service/
├── Dockerfile
├── requirements.txt
└── app/
├── main.py
├── database.py
└── models.py
Создание пользователя:
 PowerShell
$body = @{email="почта"; full_name="имя"; phone="+1234567890"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8001/api/v1/test/test-users/" -Method POST -Body $body -ContentType "application/json"
создание заказа
$body = @{
    user_id = 1
    shipping_address = @{
        city = "Город"
        street = "улица"
        building = "дом"
        apartment = "квартира"
    }
    items = @(
        @{ product_id = 1; quantity = 2; name = "наименование"; price = цена },
        @{ product_id = 2; quantity = 1; name = "Mouse"; price = 1500 }
    )
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8001/api/v1/orders/" -Method POST -Body $body -ContentType "application/json"
