### Hexlet tests and linter status:
[![Actions Status](https://github.com/ZuevSN/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ZuevSN/python-project-52/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/22676666d3cc8b7783d4/test_coverage)](https://codeclimate.com/github/ZuevSN/python-project-52/test_coverage)

# Task manager

## Описание
#
Менеджер задач - это сайт для распределения задач по пользователям. Состоит из пунктов Пользователи, Статусы, Метки и сообственно Задачи. В пункте Пользователи производятся Создание, Изменение, удаление пользователей. Справочники Статусов и Меток и пункт Задачи доступны только авторизованным пользователям. В Задачах выводится список всех имеющихся задач. Через фильтр можно ограничить выводимый список. В окне задачи указываются название, описание, статус, метки и назначается исполнитель. Инициатором задачи становится пользователь, из под которого была создана задача. Обязательны для заполнения поля Имя и Статус, причем Имя задачи должно быть уникальным. Задачу может удалить только автор и только если не указан исполнитель. Статусы, метки и пользователи могут быть удалены только если они не используются в задачах. Редактирование и удаление учетных записей пользователей доступно только соответствующим учеткам пользователям.

Для просмотра работы приложения [Проект на Render](https://python-project-52-l5uk.onrender.com)

#
Минимальыне требования: Python version 3.10; Poetry version 1.8.2
#

## Установка проекта:

1. Склонировать репозиторий
```
git clone https://github.com/ZuevSN/python-project-52.git
```
2. Установить зависимости
```
poetry install
```
3. Задать переменные окружения, заполнив файл .env (в проекте есть пример .example_env)
4. Выполнить миграции моделей в базу
```
make migrate
```
#
## Запуск проекта:
1. Запуск проекта на gunicorn
```
make start
```
2. Запуск проекта в среде разработки для отладки
```
make dev
```