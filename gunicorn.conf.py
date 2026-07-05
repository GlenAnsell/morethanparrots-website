import multiprocessing

bind = "unix:/run/gunicorn/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2

errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
capture_output = True
enable_stdio_inheritance = True

proc_name = "mtp_website"
