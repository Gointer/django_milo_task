## Instruction
1. git clone https://github.com/Gointer/django_milo_task.git

2. virtualenv milovenv
3. source milovenv/bin/activate

4. pip install -r requirements/dev.txt

5. python manage.py migrate
6. python manage.py collectstatic --noinput
7. make ci
8. python manage.py runserver

## ScreenShots

![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-37.png)
![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-43.png)
![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-54.png)
![Alt text](https://github.com/Gointer/screenshots/blob/master/Screenshot%20from%202016-04-15%2007-02-59.png)

## Release Note

  1. Created extended custom User model
  
  2. Created views for managing this model
  
  3. Created two template tags
  
  4. Created download link
  
