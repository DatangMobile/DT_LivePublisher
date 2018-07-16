# 该文件为熟悉Django创建

import sys
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.core.wsgi import get_wsgi_application


settings.configure(
    DEBUG=True,
    SECRET_KEY='sk',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.commonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


# 定义一个index函数
def index(resquest):
    return HttpResponse("Hello world")


application = get_wsgi_application()

urlpatterns = (
    url(r'^$', index),
)

# 程序入口
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
