# coding:utf-8
"""
规则说明:
调用单表接口需要指明支持的请求方法(GET,POST,PUT,DELETE),如果未指定，默认不注册该单表接口.
可以重新自定义的单表接口请求方式的处理逻辑

"""
import logging
from flask import Blueprint

bp = Blueprint("services", __name__, url_prefix="/")
logger = logging.getLogger(__name__)

@bp.route("/logs",methods=["GET"])
def test():
    logging.info("this is info")
    logging.debug("this is debug")
    logging.warning("this is warning")
    logging.error("this is error")
    logging.critical("this is critical")

    return "ok"
