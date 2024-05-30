workers = 4
bind = "0.0.0.0:8000"
chdir = "/app/backend/"
module = "api.wsgi:application"
timeout = 120
