import json
import logging
from unicodedata import name
from flask import Blueprint,request,jsonify

from flask_mongoengine.wtf import model_form

from app.models.model import Article, User
from app.utils.code import ResponseCode, ResponseMessage
from app.utils.response import ResMsg
from app.utils.util import route

bp = Blueprint("test", __name__, url_prefix="/")
logger = logging.getLogger(__name__)

@bp.route("/logs", methods=["GET"])
def test():
    logging.info("this is info")
    logging.debug("this is debug")
    logging.warning("this is warning")
    logging.error("this is error")
    logging.critical("this is critical")

    return "ok"

@route(bp, "/users", methods=["GET", "POST"])
def users():
    if request.method == 'GET':
        users = User.objects.all()
        data = [user.data for user in users]
        return data
    if request.method == "POST":
        jsons = request.get_json(force=True)
        print('add user', jsons)
        users = User.from_json(json.dumps(jsons))
        users.save()
        return 'success'

PostForm = model_form(Article, base_class=object, only=['title', 'content'])
@route(bp, "/articles", methods=["GET", "POST", "DELETE"])
def articles():
    if request.method == 'GET':
        articles = Article.objects.all()
        print('articles', articles)
        data = [article.data for article in articles]
        return data
    if request.method == 'POST':
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
    if request.method == 'DELETE':
        jsons = request.get_json(force=True)
        Article.from_json(json.dumps(jsons)).delete()
        return 'success'