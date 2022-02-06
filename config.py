import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# До создания класса Config импортируем файл .env 
# чтобы переменные файла .env были уже установлены при создании класса Config
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # секретный ключ берется из переменной SECRET_KEY если она не определена  
    # берется жестко запрограммированная строка 'you-will-never-guess'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # расположения базы данных берется из переменной среды DATABASE_URL если она не определенна 
    # настраиваем базу данных с именем app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # отключаем отправку сигнала приложению каждый раз,
    # когда в базу данных должно быть внесено изменение
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # данные почтового сервера на который будет отправляться ошибки
    # с трассировкой стека ошибки в теле письма.
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS - список адресов которые будут получать отчеты об ошыбках
    ADMINS = ['your-email@example.com']

    # Запуск поддельного почтового сервера SMTP который принимает электронные письма,
    # но вместо того, чтобы отправлять их, выводит их в консоль.
    # python -m smtpd -n -c DebuggingServer localhost:8025
    # export MAIL_SERVER=localhost
    # export MAIL_PORT=8025

    # Пример для отправки писем на почту google
    # export MAIL_SERVER=smtp.googlemail.com
    # export MAIL_PORT=587
    # export MAIL_USE_TLS=1
    # export MAIL_USERNAME=<your-gmail-username>
    # export MAIL_PASSWORD=<your-gmail-password>

    # количества постов на странице.
    POSTS_PER_PAGE = 3

    # список поддерживаемых языков.
    LANGUAGES = ['en', 'ru']

    # добавьте ключ Microsoft Translator API в конфигурацию.
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    # Elasticsearch -  Полнотекстовый поиск
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    # URL-адрес подключения для службы Redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'