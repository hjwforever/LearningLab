import datetime
import decimal
import uuid
from bson import ObjectId
from flask.json import JSONEncoder as BaseJSONEncoder

# from flask_apscheduler import APScheduler

# scheduler = APScheduler()



class JSONEncoder(BaseJSONEncoder):

    # BaseJSONEncoder 默认支持格式化高精度数字 decimal.Decimal
    # BaseJSONEncoder 默认支持格式化uuid uuid.UUID
    def default(self, o):
        """
        :param o:
        :return:
        """
        # 格式化ObjectId
        # if hasattr(o, 'password'):
        #     del o.password
        #     return o
        if isinstance(o, ObjectId):
            return str(o)
        # 格式化时间
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        # 格式化日期
        if isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')
        # 格式化字节数据
        if isinstance(o, bytes):
            return o.decode("utf-8")