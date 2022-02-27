import os
import yaml
import logging
import logging.config
from flask import Blueprint, Flask

from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension
from app.utils.core import JSONEncoder, db

from app.api.router import router

def create_app(config_name, config_path=None):
    app = Flask(__name__)

	# 配置文件默认路径与模式
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'config/config.yaml')
    if not config_name:
        config_name = 'PRODUCTION'

	# 读取配置文件
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)
    # print('config', conf)

    # 注册数据库
    db.init_app(app)
    print('db', db, conf['MONGODB_DEBUG'])
    if conf['MONGODB_DEBUG']:
        app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
        toolbar = DebugToolbarExtension(app)
        print('toolbar', toolbar)

    # 注册接口
    register_api(app=app, routers=router)

    # 返回json格式转换
    app.json_encoder = JSONEncoder

    # 响应信息设置
    with open(app.config['RESPONSE_MESSAGE_CONFIG_PATH'], 'r', encoding='utf-8') as f:
        msg_conf = yaml.safe_load(f.read())
    app.config.update(msg_conf)

    # 日志文件目录
    if not os.path.exists(app.config['LOGGING_PATH']):
        os.mkdir(app.config['LOGGING_PATH'])

    # 日志配置
    with open(app.config['LOGGING_CONFIG_PATH'], 'r', encoding='utf-8') as f:
        dict_conf = yaml.safe_load(f.read())

    return app

def read_yaml(config_name, config_path):
    """
    config_name: 需要读取的配置环境内容
    config_path: 配置文件路径
    """
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('未找到对应的配置信息')
    else:
        raise ValueError('请输入正确的配置名称或配置文件路径')

def register_api(app, routers):
    for router_api in routers:
        if isinstance(router_api, Blueprint):
            app.register_blueprint(router_api)
        else:
            try:
                endpoint = router_api.__name__
                view_func = router_api.as_view(endpoint)
                # 如果没有服务名,默认 类名小写
                if hasattr(router_api, "service_name"):
                    url = '/{}/'.format(router_api.service_name.lower())
                else:
                    url = '/{}/'.format(router_api.__name__.lower())
                if 'GET' in router_api.__methods__:
                    app.add_url_rule(url, defaults={'key': None}, view_func=view_func, methods=['GET', ])
                    app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['GET', ])
                if 'POST' in router_api.__methods__:
                    app.add_url_rule(url, view_func=view_func, methods=['POST', ])
                if 'PUT' in router_api.__methods__:
                    app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['PUT', ])
                if 'DELETE' in router_api.__methods__:
                    app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['DELETE', ])
            except Exception as e:
                raise ValueError(e)