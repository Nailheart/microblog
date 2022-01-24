from app import app, db
from app.models import User, Post

# Декоратор app.shell_context_processor регистрирует функцию как функцию контекста оболочки. Когда flask shellкоманда запустится, она вызовет эту функцию и зарегистрирует возвращенные ею элементы в сеансе оболочки
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
