#### 启动 celery
```angular2html
在 celery_demo 目录上一层执行以下命令
celery -A celery_demo.celery_app worker -l=info
参数 -A 指定了 Celery 实例的位置

启动调度器调度任务
celery beat -A celery_demo.celery_app -l=info

连续启动 worker 进程和 beat 进程
celery -B -A celery_demo.celery_app worker --loglevel=info

```
#### 启动 flower
```angular2html
celery flower -A celery_demo.celery_app worker --address=127.0.0.1 --port=5555 -l=info
```

