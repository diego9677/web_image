import multiprocessing

command = '/home/ubuntu/django_env/bin/gunicorn'
pythonpath = '/home/ubuntu/web_image'
bind = '152.44.40.128:8000'
workers = multiprocessing.cpu_count() * 2 + 1
