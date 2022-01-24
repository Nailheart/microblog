from datetime import datetime
from app import db

# класс User наследуется от db.Model базового класса для всех моделей
class User(db.Model):
    # Поля создаются как экземпляры db.Column класса, который принимает тип поля в качестве аргумента, а также другие необязательные аргументы, которые, например, позволяют указать, какие поля являются уникальными и проиндексированы, что важно для эффективного поиска в базе данных.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Метод __repr__ сообщает Python, как печатать объекты этого класса
    def __repr__ (self):
      return '<User {}>'.format(self.user)


# класс Post представлет сообщения в блогах, написанные пользователями.
class Post():
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__ (self):
      return '<Post {}>'.format(self.body)