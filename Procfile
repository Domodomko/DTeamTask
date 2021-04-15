web: gunicorn --pythonpath DTeamTask DTeamTask.wsgi
worker: sh -c 'cd DTeamTask && celery -A DTeamTask worker --beat -l INFO --pool=solo'