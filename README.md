# DTeam Task
## Made by Sergei Shinn
## [Deployed Heroku](https://dteamtask.herokuapp.com)
A Django app made as a test task for a Backend-developer vacancy.  
It allow to get the news list, authors and generates new news itself every 5 minutes.  
It has API for geting, posting, patching and deleting news.


## About Developing

- The task was written in 1 day
- First time working with Celery and Redis
- First time working with pipenv


## Link Structure

Here's some kind of documentation for this app:  
  
**The Main Page has products categories and subcategories on it**

- **/** - Home
- **/news** - News List
- **/authors** - Authors List
- **/api** - API part of the App
    - **/news** - API News List
    - **/news/(pk)** - API News Item (GET, PUT, PATCH, DELETE)
    - **/news_create** - API Create News (POST)
- **/admin** - Admin panel
- **/swagger** - Swagger API Page
- **/redoc** - Redoc API Page


## Installation
##### *This instruction is written for Linux users*
After pushing this repository and creating your DB on Postgre, you'll need to create new python venv for it and install requirements:

```sh
python3 -m venv /venv
pip install -r requirements.txt
```
Create settings .env file with these variables inside:
- DEBUG
- SECRET_KEY
- DATABASE_URL
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- CELERY_TIMEZONE
- CELERY_TASK_TRACK_STARTED
- CELERY_TASK_TIME_LIMIT
- CELERY_BROKER_UR


After that you'll need to migrate the data, create a superuser and run the application:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Launching celery:

```sh
celery -A DTeamTask beat
celery -A DTeamTask worker -l INFO --pool=solo
```
