# -*- coding: utf-8 -*-

import sys

sys.path.append("./")
from celery_demo.celery_app import task1
from celery_demo.celery_app import task2

# 也可用 task1.add.delay(1, 2)
task1.add.delay(1, 2)

# 也可用 task2.multiply.apply_async(3, 4)
task2.multiply.delay(3, 4)
print '=========== end ==========='
