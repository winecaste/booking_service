# Booking service
## Run service
1. Скопируй репозиторий

```bash
git clone https://github.com/yourusername/booking_service.git
```
2. Перейди в папку ```cd booking_service```

3. Установи зависимости

```bash
python -m venv venv
source venv/bin/activate  # для Unix/Mac
.\venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```
4. Переименовать файл .env-example --> .env и заполнить его.

5. Настроить базу данных и конфигурацию в файле config.py.

6. Запустить приложение:
```bash
uvicorn app.main:app --reload
```
### Celery & Flower
Для запуска Celery используется команда  
```
celery --app=app.tasks.celery:celery worker -l INFO -P solo
```
Обратите внимание, что `-P solo` используется только на Windows, так как у Celery есть проблемы с работой на Windows.  
Для запуска Flower используется команда  
```
celery --app=app.tasks.celery:celery flower
``` 

Они уже включены в настройки запуска докер контейнера

### Dockerfile
Если вы меняли что-то внутри Dockerfile, то есть меняли логику составления образа
Запустите команду ```docker build .```

### Sentry
Для настройки логирования зарегистрируйтесь на [офф.сайте](https://sentry.io/welcome/) или зайдите через гугл/гитхаб
Выберите фреймворк своего проекта и скопируйте sentry_dns, который вам предложат и введите его в .env-non-dev файл.


### Grafana / Prometheus

1. Для входа в кабинет нужно указать ```username: admin, password: admin```
2. Потом переопределить пароль
3. Чтобы заработали графики вы должны в grafana-dashboard указать свой uid в следующем куске кода:
```"datasource":{"type": "prometheus","uid": "ВАШ UID"} ```
4. Взять его можно из json-схемы предустановленных дашбордов  
   (в настройках add data source -> prometheus -> "выбираем имя").
Затем в Dashboards -> import -> Вставляем содержимое grafana-dashboard.json и выбираем какой-нибудь случайный uuid(и имя для дашборда)
5. Если не интересуют метрики / логирование можно отключить закоментировав строчки с sentry и instumentator в файле app/main.py и docker-compose
   
### Функциональности

- Регистрация и аутентификация пользователей.
- Получение списка отелей и комнат.
- Бронирование номеров.
