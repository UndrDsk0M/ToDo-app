# ToDo-app
<img width="1333" height="855" alt="title" src="https://github.com/user-attachments/assets/b94069cd-151d-421a-b022-792f987b208a" />

A versatile ToDo site built with Django and JavaScript that lets you write and save tasks both online and offline, complete with user authentication support. this app allows users to create and delete, and track tasks with ease.
Features

## features
+ Add Tasks: Quickly create new tasks with descriptions and due dates.
+ Online & Offline Task Management: manage tasks whether you're connected or offline.
+ Delete Tasks: Remove tasks that are no longer needed.
+ User Authentication: Secure user accounts with login, registration, and session management.
+ Responsive Design: Works seamlessly on desktop and mobile devices
+ Dark and Ligth Mode :
<img width="256" height="128" alt="lightmode" src="https://github.com/user-attachments/assets/c87879b1-8a56-4f7c-a737-f4574881f70d" />
<img width="256" height="128" alt="darkmode" src="https://github.com/user-attachments/assets/b94069cd-151d-421a-b022-792f987b208a" />


.
[Optional: Add any unique features, e.g., Task Categories, Filtering, or Local Storage]

---
## Tech Stack
| Component | Technologies |
|---------------|------------------------|
| Backend/API | Django (Python) |
| Frontend UI | JavaScript, HTML, CSS |
| Offline Sync | Browser storage/Web APIs (e.g., localStorage or Service Workers) |
---
0. [features](#features)
1. [Installation](#installation)
2. [Usage](#usage)
3. [Live View](#view)
5. [Contributing](#contributing)
6. [License](#license)


## Installation
Follow these steps to set up the ToDo app locally:
Steps

### Clone the Repository:
```
git clone https://github.com/UndrDsk0M/ToDo-app.git
cd ToDo-app
```

### Install Dependencies:
```
pip install -r requirements.txt
```

### Run the Application:
```
python manage.py runserver 127.0.0.1:80000
```

Open your browser and navigate to http://localhost:[port] (default: [e.g., 3000 or 8000]).
( also you can run python manage.py migrate if needed )


## Usage

+ <b>Create a Task</b>: Enter task details in the input field and click "Add" or press Enter.
+ <b>Delete a Task</b>: Click the delete icon to remove a task.
+ <b>Create local account</b>: enter the sign in/up and enter the captcha, username and password
+ <b>Mark Complete</b>: Check the box next to a task to mark it as complete.

## view
not deployed yet.

## Project Structure
```
todo/ – Core Django app containing models, views, forms, and templates.
templates/ – Shared HTML templates for rendering pages.
static/ – Frontend assets: CSS, JavaScript, images, etc.
data/ – Storage for database files or other runtime-generated data (e.g., db.sqlite3).
manage.py – Django’s management script for running commands.
```

## Contributing
Contributions are highly appreciated! Whether it’s bug fixes, feature enhancements, or documentation improvements:

Fork the repo

Create a new branch (git checkout -b feature/awesome-feature)

Make your changes and commit (git commit -m "Add awesome feature")

Push to your branch (git push origin feature/awesome-feature)

Open a Pull Request with a clear description


Please ensure your code follows the project's coding standards and includes relevant tests.
## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this application as you see fit.
Contact
For questions or feedback, reach out to UndrDsk0M.
Also the base of the front-end was built by <a href="https://tamana543.github.io/portfolio">Tamana <ReginaJS/></a> and the back-end was built by <a href="https://gravatar.com/fantasticcherryblossomef40d159a8">Me!</a>
thanks everyone for supporting and helping this project.
