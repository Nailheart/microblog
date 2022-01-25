from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# класс User наследуется от db.Model базового класса для всех моделей
class User(UserMixin, db.Model):
    # Поля создаются как экземпляры db.Column класса, который принимает тип поля в качестве аргумента, а также другие необязательные аргументы, которые, например, позволяют указать, какие поля являются уникальными и проиндексированы, что важно для эффективного поиска в базе данных.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # метод __repr__ сообщает Python, как печатать объекты этого класса
    def __repr__ (self):
        return '<User {}>'.format(self.user)

    # хэширование и проверка пароля.
    def set_password(self, password):
      self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Пользовательский загрузчик регистрируется в Flask-Login с помощью декоратора @login.user_loader.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# класс Post представлет сообщения в блогах, написанные пользователями.
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__ (self):
        return '<Post {}>'.format(self.body)
