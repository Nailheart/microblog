from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

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

from app import views, models
