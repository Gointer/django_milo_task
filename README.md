git clone https://github.com/Gointer/django_milo_task.git

virtualenv milovenv
source milovenv/bin/activate

pip install -r requirements/dev.txt

python manage.py migrate
python manage.py collectstatic --noinput

python manage.py runserver

