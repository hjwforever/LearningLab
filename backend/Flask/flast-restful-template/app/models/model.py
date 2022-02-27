from flask_mongoengine import *
from app.utils.core import db

class User(db.Document):
    """
    用户表
    """
    meta = {'collection': 'users'}
    email = db.StringField(required=True)
    username = db.StringField(required=True, max_length=128, unique=True)
    password = db.StringField(required=True, min_length=6, max_length=16)

    def __repr__(self):
        return 'User(username="{}", email="{}")'.format(self.username, self.email)

    @property
    def data(self):
        _data = dict(id=self.id, #id=str(self.id),
                    username=self.username,
                    email=self.email)
        return _data

class Article(db.Document):
    """
    文章表
    """
    meta = {'collection': 'articles'}
    title = db.StringField(required=True)
    content = db.StringField(required=True)
    author = db.ReferenceField(User)
    create_time = db.DateTimeField()
    update_time = db.DateTimeField()

    def __repr__(self):
        return 'Article(author="{}", title="{}", content="{}")'.format(self.author, self.title, self.content)

    @property
    def data(self):
        _data = dict(id=self.id,
                    title=self.title,
                    content=self.content,
                    author=self.author,
                    create_time=self.create_time,
                    update_time=self.update_time)
        return _data