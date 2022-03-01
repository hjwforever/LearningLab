import json
from flask import Blueprint,request
from flask_restful import Resource, Api
from app.utils.response import ResMsg
from app.models.model import Article, User
from mongoengine import errors

bp = Blueprint("articles", __name__, url_prefix="/articles")
api = Api(bp)

class Articles(Resource):
    def get(self, id=""):
        if id == "":
            articles = Article.objects.all()
            data = [article.data for article in articles]
            return ResMsg.success(data)
        else:
            article = Article.objects.get(id=id)
            return ResMsg.success(article.data)
    def post(self):
        jsons = request.get_json(force=True)
        user_id = jsons.pop('user_id')
        print('jsons', jsons)
        user = User.objects.get(id=user_id)
        print('user', user.data)
        articel = Article.from_json(json.dumps(jsons))
        print('articel0', str(articel), articel.author)
        articel.author = user
        articel.save()
        print('articel',str(articel))
        return 'success'
    def delete(self, id):
        try:
            article = Article.objects.get(id=id)
            print('delete article', article.data)
            if article:
                article.delete()
                return ResMsg.success()
            else:
                return ResMsg.error('article not found or has been deleted')
        except errors.ValidationError:
            return ResMsg.error(msg="id is not valid")
    def put(self, id):
        try:
            article = Article.objects.get(id=id)
            jsons = request.get_json(force=True)
            print('update article', jsons)
            article.update(**jsons)
            return ResMsg.success(msg=f"article<id={id}> has been updated")
        except errors.ValidationError:
            return ResMsg.error(msg="id or article detail is not valid")

api.add_resource(Articles, "", "/<string:id>")