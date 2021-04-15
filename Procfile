web: gunicorn --pythonpath DTeamTask DTeamTask.wsgi
beat: celery -A DTeamTask beat
celery: celery -A DTeamTask worker -l INFO --pool=solo