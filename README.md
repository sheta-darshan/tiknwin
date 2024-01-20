
Game Prediction App
Welcome to the Game Prediction App - your first project using the Django framework! This application allows users to predict the winner of a game, earn points for correct predictions, and participate in a lucky draw based on accumulated points.

How It Works
Users can make game winner predictions, and based on the accuracy of their predictions, they will earn points. A lucky draw will be conducted periodically, and the winners will be announced. It's important to note that there is no monetary involvement in this site; it's all about having fun and testing your game prediction skills.

Getting Started Locally
To set up the project on your local machine using Visual Studio Code, follow these instructions:

Remove the existing db.sqlite3 file.
Delete all migration files in the migrations folder, starting from those named 000.
Open a terminal and run the following commands:
bash
Copy code
pip install -r requirements.txt
python manage.py migrate
To create an admin account for managing the application, generate a user ID and password by running:
bash
Copy code
python manage.py createsuperuser
Finally, start the app in your browser using the following command:
bash
Copy code
python manage.py runserver
Contributing
If you'd like to contribute to the development of this project, feel free to fork the repository and submit a pull request. We welcome your ideas and contributions to make this app even better!

License
This project is licensed under the MIT License - feel free to use, modify, and distribute the code as needed. Happy predicting!