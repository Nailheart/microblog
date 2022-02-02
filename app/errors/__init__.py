from flask import Blueprint

bp = Blueprint('errors', __name__)

# После создания объекта blueprint импортирем модуль handlers.py,
# чтобы обработчики ошибок в нем были зарегистрированы в blueprint.
# Этот импорт находится внизу, чтобы избежать циклических зависимостей.
from app.errors import handlers
