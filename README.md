# Проект Ретранслятор JSON

### [Документация Swagger](http://127.0.0.1:8000/swagger_docs)
### [Логи](./logs/file_1.log)
### [Тесты](./tests)
### [Переменное окружение](./.env)
### [Зависимости](./requirements.txt)

## Запуск Проекта:
```shell
docker compose -f docker-compose.dev.yml up -d
```

## Настройка RabbitMQ:
1. Авторизуемся в [панели](http://127.0.0.1:15672/)
2. Переходим в вкладку <b>Queues and Streams</b>
3. Создаем очередь с названием, которое указано в .env в переменной: <b>RABBITMQ_QUEUE</b>

## Python Версия: ```3.12.0```