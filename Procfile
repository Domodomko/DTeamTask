web: gunicorn --pythonpath DTeamTask DTeamTask.wsgi
worker: sh -c 'cd DTeamTask && celery -A DTeamTask worker -l INFO --pool=solo'
beat: sh -c 'cd DTeamTask && celery -A DTeamTask beat'