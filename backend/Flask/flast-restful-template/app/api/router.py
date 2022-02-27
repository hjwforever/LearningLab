from app.api.api_test import bp as bp_api_test
from app.api.services import bp as bp_services

router = [
    bp_api_test, # 接口测试
    bp_services,
]