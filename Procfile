web: gunicorn --pythonpath DTeamTask DTeamTask.wsgi
beat: celery -A DTeamTask beat
worker: celery -A DTeamTask worker -l INFO --pool=solo