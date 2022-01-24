from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Берем настройки конфигурации из класса Config (/config.py)
app.config.from_object(Config)

# обьект представляющий базу данных
db = SQLAlchemy(app)

# обьект представляющий механизм миграции
migrate = Migrate(app, db)

from app import views, models
