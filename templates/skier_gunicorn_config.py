import multiprocessing

bind = "{{ skier_gunicorn_bind_addr }}"
chdir = "{{ skier_install_dir }}"
workers = multiprocessing.cpu_count() * 2 + 1

# Choose one as appropriate.
worker_class = "sync"
# worker_class = "gthread" # Python 3 only.
# worker_class = "gevent"
# worker_class = "eventlet"
# worker_class = "tornado"

# Change to false to disable daemonising.
# daemon = True
daemon = {{ skier_gunicorn_is_daemon }}

# Change to specify the user gunicorn will run as.
user = "{{ skier_proc_user }}"
# Change to specify the group gunicorn will run as.
group = "{{ skier_proc_group }}"

# SSL settings.
# If you are running the server without a reverse proxy (nginx or apache), this is highly recommended.

# keyfile = "ssl/server.key"
# certfile = "ssl/server.crt"

accesslog = "{{ skier_log_dir }}/access.log"
errorlog = "{{ skier_log_dir }}/error.log"

def when_ready(server):
    print("Server ready on address {}.".format(bind))
