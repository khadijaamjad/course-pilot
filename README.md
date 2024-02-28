# CoursePilot - Embark on your learning journey!

CoursePilot is your personal guide to seamless online learning. Discover courses, give tests, and soar through your educational journey.

This project was developed as part of the **Django Application Development with SQL and
Databases** course by IBM. 

## 🚀 Features

- **Sign-up and Sign-in**: Create an account to keep track of your courses and tests.
- **Enrolment**: Enrol in multiple courses at a time.
- **Result After Each Test**: When you finish a test, you get the score and correct answers.
- **Retest**: You can give tests again to improve results.
- **Admin Mode**: With the Django Admin mode, you can manage your data from the UI without having to interact with the DB.

## 🛠️ Technologies

- `Django`
- `Python`
- `SQLite`
- `Django ORM`
- `Bootstrap`

## 🚦 Running the Project

To run the project in your local environment, follow these steps:

1. Clone the repository to your local machine.
2. Run `py -m ensurepip` to confirm that pip is installed.
3. Install Django using `py -m pip install Django`
4. Run migrations before running the app `py manage.py makemigrations` then `py manage.py migrate`
5. Finally, start the server using `py manage.py runserver`
6. Open [http://localhost:8000](http://localhost:8000) to view the app.


### Accessing Admin Pages
1. To access the admin pages, create a super user with the command `py manage.py createsuperuser`
2. Provide a username, email and password in the terminal
3. Start the server and navigate to [http://localhost:8000/admin](http://localhost:8000/admin) and use the credentials from step 2 to sign in. 

## 💡 Improvements

- **Dashboard**: Add a dashboard with statistics to give an overview of ongoing and completed courses. 
- **Better UI design**: Improve the UI with some libraries.
- **Dark Mode**: Add support for dark mode. 
