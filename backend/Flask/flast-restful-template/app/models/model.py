from flask_mongoengine import *
from mongoengine import Document, StringField,ReferenceField,DateTimeField

class User(Document):
    """
    用户表
    """
    meta = {'collection': 'users'}
    email = StringField(required=True)
    username = StringField(required=True, max_length=128, unique=True)
    password = StringField(required=True, min_length=6, max_length=16)

    def __repr__(self):
        return 'User(username="{}", email="{}")'.format(self.username, self.email)

    @property
    def data(self):
        _data = dict(id=self.id, #id=str(self.id),
                    username=self.username,
                    email=self.email)
        return _data

class Article(Document):
    """
    文章表
    """
    meta = {'collection': 'articles'}
    title = StringField(required=True)
    content = StringField(required=True)
    author = ReferenceField(User)
    create_time = DateTimeField()
    update_time = DateTimeField()

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