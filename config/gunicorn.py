import multiprocessing

command = '/home/ubuntu/django_env/bin/gunicorn'
pythonpath = '/home/ubuntu/web_image'
bind = '209.50.59.250'
workers = multiprocessing.cpu_count() * 2 + 1
