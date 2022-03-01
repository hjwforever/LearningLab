from app.api.api_test import bp as bp_api_test
from app.api.users import bp as users_api
from app.api.articles import bp as articles_api
from app.api.services import bp as bp_services

router = [
    bp_api_test, # 接口测试
    users_api, # 用户
    articles_api, # 文章
    bp_services,
]