this is my first project using django framework

in this project prediction of game winner will be provided by player. on their prediction basis they will get points if their prediction is right.

on the basis of points lucky draw will be conducted and winners will anounce.

# There is no money involve in this site for playing.

to start instruction on local pc via visual studio code

remove db.sqlite3 file
remove all migrations folder files which starts from 000
run this commands
python manage.py makemigrations app
python manage.py migrate
# for statrting admin accounts genrate user id and password
python manage.py createsuperuser
# to strt app in your browser
python manage.py runserver 

