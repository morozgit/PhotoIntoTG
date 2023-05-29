# Космический Телеграм

Скачивает красивые фото NASA и выкладывает в телеграмм канал 

## Установка 

### Установка python
   
#### Для Linux 
```
sudo apt-get install python3
```
#### Для Mac OC
```
brew install python3
```
## Репозиторий
Клонируйте репозиторий в удобную папку

## Окружение

### Библиотеки

В терминале перейдите в папку с репозиторием

Установите библиотеки с помощью команды
```python 
pip3 install -r requirements.txt
```

### Переменные окружения 
#### Получение API-токена NASA
* Получить можно на [сайте](https://api.nasa.gov/).

#### Запись API-токена NASA
```python
echo NASA_TOKEN=ваш токен > .env
```

## Запуск fetch_spacex_images

Передайте в виде аргумента ID запуска. Если ID запуска не указан, то скачаются фото с последнего запуска.
```python
python3 fetch_spacex_images.py -id ID запуска
```

## Запуск nasa_apod_photo

Передайте в виде аргумента дату с которой начать скачивать фото.
```python
python3 nasa_apod_photo.py YYYY-MM-DD
```

## Запуск nasa_epic_photo

Скачается эпичное фото
```python
python3 nasa_epic_photo.py 
```

## Запуск Telegram bot

### Регистрация бота и получения API-токена

* Пройти по [ссылке](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)
и все получится.

#### Запись API-токена Telegram
```python
echo TG_TOKEN=ваш токен >> .env
```

#### Запись chat_id Telegram
```python
echo CHAT_ID=ваш chat_id >> .env
```

### Запуск nasa_telegram_bot. Фото будут выкладываться в 

##### Фото из папки images будут выкладываться в канал с интервалом по умолчанию 4 часа 

```python
python3 nasa_telegram_bot.py -t время в минутах
```

## Enjoy your chanel