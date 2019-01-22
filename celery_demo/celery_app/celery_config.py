# -*- coding: utf-8 -*-

from datetime import timedelta
from celery.schedules import crontab

# 指定 Broker
BROKER_URL = 'redis://'

# 指定 Backend
CELERY_RESULT_BACKEND = 'redis://'

# 指定时区，默认是 UTC
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_ACCEPT_CONTENT = ['json']

# 指定导入的任务模块
CELERY_IMPORTS = (
    'celery_demo.celery_app.task1',
    'celery_demo.celery_app.task2'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_demo.celery_app.task1.add',
        'schedule': timedelta(seconds=5),  # 每 5 秒执行一次
        'args': (5, 8)  # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_demo.celery_app.task2.multiply',
        'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
        'args': (3, 7)  # 任务函数参数
    }
}
