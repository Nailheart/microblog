import logging
from logging.handlers import SMTPHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)

# Берем настройки конфигурации из класса Config (/config.py)
app.config.from_object(Config)

# обьект представляющий базу данных
db = SQLAlchemy(app)

# обьект представляющий механизм миграции
migrate = Migrate(app, db)

# инициализация Flask-логин
login = LoginManager(app)

# Значение 'login' это имя функции (или конечной точки) для входа в систему. Другими словами, имя, которое вы будете использовать в url_for() вызове для получения URL-адреса.
login.login_view = 'login'

# Журнал ошыбок по электроной почте
# включаем регистратор электронной почты только тогда, когда приложение работает без режима отладки, что обозначается app.debug как True, а также когда почтовый сервер существует в конфигурации.
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    secure = None
    if app.config['MAIL_USE_TLS']:
        secure = ()
    mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr='no-reply@' + app.config['MAIL_SERVER'],
        toaddrs=app.config['ADMINS'], subject='Microblog Failure',
        credentials=auth, secure=secure)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

    # создаем каталог журналов если его не существует и записываем файл журнала с именем microblog.log
    # ограничиваем размер файла журнала до 10 КБ и сохраняем последние десять файлов журнала в качестве резервной копии.
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import views, models, errors
