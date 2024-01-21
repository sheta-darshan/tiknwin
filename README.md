# Game Prediction App

Welcome to the Game Prediction App - your first project using the Django framework! This application allows users to predict the winner of a game, earn points for correct predictions, and participate in a lucky draw based on accumulated points.

## How It Works

Users can make game winner predictions, and based on the accuracy of their predictions, they will earn points. A lucky draw will be conducted periodically, and the winners will be announced. It's important to note that there is no monetary involvement in this site; it's all about having fun and testing your game prediction skills.

## Getting Started Locally

To set up the project on your local machine using Visual Studio Code, follow these instructions:

1. Remove the existing `db.sqlite3` file.
2. Delete all migration files in the `migrations` folder, starting from those named `000`.
3. remove all media files in folders do not delete folder
4. download install Python 3.11.5 for windows pc via this link https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe if not installed
5. intall pip if not installed
6. Open a terminal and run the following commands:


```powershell
pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate

#To create an admin account for managing the application, generate a user ID and password by running:
python manage.py createsuperuser

#Finally, start the app in your browser using the following command:
python manage.py runserver

#Contributing
#If you'd like to contribute to the development of this project, feel free to fork the repository and submit a pull request. We welcome your ideas and contributions to make this app even better!
