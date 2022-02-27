from calendar import c
from flask import request, current_app

from app.utils.code import ResponseCode


class ResMsg(object):
    """
    封装响应文本
    """
    def __init__(self, data=None, code=ResponseCode.Success, rq=request):
        # 获取请求中语言选择,默认为中文
        self.lang = rq.headers.get("lang",current_app.config.get("LANG", "zh_CN"))
        self.external = {}
        self._data = data
        self._msg = current_app.config[self.lang].get(code, None)
        self._code = code

    def update(self, data=None, code=None, msg=None):
        """
        更新默认响应文本
        :param code:响应编码
        :param data: 响应数据
        :param msg: 响应消息
        :return:
        """
        if code is not None:
            self._code = code
            # 获取对应语言的响应消息
            self._msg = current_app.config[self.lang].get(code, None)
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name in ['data', 'msg', 'code']:
            print('name cannot in ["data", "msg", "code"]')
        elif name is not None and value is not None:
            self.external[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        _dict = self.__dict__
        body = dict(code = _dict["_code"],
                    msg = _dict["_msg"],
                    data = _dict["_data"])
        if self.external:
            body.update(self.external)
        return body
