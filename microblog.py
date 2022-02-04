from app import create_app, db, cli
from app.models import User, Post, Message, Notification

app = create_app()
cli.register(app)

# Декоратор app.shell_context_processor регистрирует функцию как функцию контекста оболочки.
# Когда flask shell команда запустится, она вызовет эту функцию и зарегистрирует 
# возвращенные ею элементы в сеансе оболочки.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification}
