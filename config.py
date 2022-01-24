import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # секретный ключ берется из переменной SECRET_KEY если она не определена берется жестко запрограммированная строка
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # расположения базы данных берется из переменной среды DATABASE_URL если она не определенна настраиваем базу данных с именем app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    # отключаем отправку сигнала приложению каждый раз, когда в базу данных должно быть внесено изменение
    SQLALCHEMY_TRACK_MODIFICATIONS = False 