import multiprocessing
import socket

command = '/home/ubuntu/django_env/bin/gunicorn'
pythonpath = '/home/ubuntu/web_image'
bind = socket.gethostbyname(socket.gethostname())
workers = multiprocessing.cpu_count() * 2 + 1
