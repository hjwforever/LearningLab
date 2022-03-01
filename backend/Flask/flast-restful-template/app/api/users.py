import json
from flask import Blueprint,request
from flask_restful import Resource, Api
from app.utils.response import ResMsg
from app.models.model import User
from mongoengine import errors

bp = Blueprint("users", __name__, url_prefix="/users")
api = Api(bp)

class Users(Resource):
    def get(self, id=""):
        if id == "":
            users = User.objects.all()
            data = [user.data for user in users]
            return ResMsg.success(data)
        else:
            user = User.objects.get(id=id)
            return ResMsg.success(user.data)
    def post(self):
        jsons = request.get_json(force=True)
        print('add user', jsons)
        user = User.from_json(json.dumps(jsons))
        user.save()
        return  ResMsg.success(user.data)
    def delete(self, id):
        try:
            user = User.objects.get(id=id)
            print('delete user', user.data)
            if user:
                user.delete()
                return ResMsg.success()
            else:
                return ResMsg.error('user not found or has been deleted')
        except errors.ValidationError:
            return ResMsg.error(msg="id is not valid")
    def put(self, id):
        try:
            user = User.objects.get(id=id)
            jsons = request.get_json(force=True)
            print('update user', jsons)
            user.update(**jsons)
            return ResMsg.success(msg=f"user<id={id}> has been updated")
        except errors.ValidationError:
            return ResMsg.error(msg="id or user info is not valid")

api.add_resource(Users, "", "/<string:id>")