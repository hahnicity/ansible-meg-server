import multiprocessing

bind = "{{ megserver_gunicorn_bind_addr }}"
workers = multiprocessing.cpu_count() * 2 + 1

raw_env = [
    "MEG_SERVER_CFG={{ megserver_config_dir }}/config.yml",
    "MEG_SERVER_DEFAULT_CFG={{ megserver_install_dir }}/venv/config/config.default.yml"
]

# Choose one as appropriate.
worker_class = "sync"

# Change to specify the user gunicorn will run as.
user = "{{ megserver_proc_user }}"
# Change to specify the group gunicorn will run as.
group = "{{ megserver_proc_group }}"

# SSL settings.
# If you are running the server without a reverse proxy (nginx or apache), this is highly recommended.

# keyfile = "ssl/server.key"
# certfile = "ssl/server.crt"

accesslog = "{{ megserver_log_dir }}/access.log"
errorlog = "{{ megserver_log_dir }}/error.log"
