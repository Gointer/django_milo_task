git clone https://github.com/Gointer/django_milo_task.git

virtualenv milovenv
source milovenv/bin/activate

pip install -r requirements/dev.txt

python manage.py migrate
python manage.py collectstatic --noinput

python manage.py runserver

![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-37.png)
![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-43.png)
![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-54.png)
![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-59.png)

Release Note:

  Created extended custom User model
  
  Created views for managing this model
  
  Created two template tags
  
  Created download link
  
