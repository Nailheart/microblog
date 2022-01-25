import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # секретный ключ берется из переменной SECRET_KEY если она не определена берется жестко запрограммированная строка
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # расположения базы данных берется из переменной среды DATABASE_URL если она не определенна настраиваем базу данных с именем app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    # отключаем отправку сигнала приложению каждый раз, когда в базу данных должно быть внесено изменение
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # данные почтового сервера на который будет отправляться ошибки с трассировкой стека ошибки в теле письма.
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']