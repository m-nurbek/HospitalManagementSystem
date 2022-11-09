# Hospital Management System 🏥
### Project Milestone 2

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Hospital Management System is an application for managing data about processes in a medical organization. It manages data about Doctors and Patiens and their interaction. It currently has 3 classes of users, which are admins, doctors and patients.

> __Admins__ 💻 - have absolute access to all functions and data.
> __Doctors__ 👨‍⚕️- can manage data about patients.
> __Patients__ 🤒 - a class that stores info about patients.


## Features

- Add, delete, update data about patients and doctors
- Register and login system for all actors

## Tech stack

- [HTML] - markup language for documents designed to be displayed in a web browser.
- [Python](https://www.python.org/) - a high-level, general-purpose programming language.
- [Django](https://docs.djangoproject.com/en/4.1/) - a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.
- [SQLite](https://www.sqlite.org/index.html) - a database engine written in the C programming 

## Installation
To install the application, the repository needs to be cloned to your desktop:
```sh
git clone https://github.com/Rickserd/SWEProject.git
```

Make sure you have Python installed on your device.
Then, create a virtual environment:
```sh
python -m venv venv
```
And install all packages from the requirement.txt file:
```sh
pip install -r requirement.txt
```

To run the application, navigate to the root folder ("realapp") in terminal and run the following command:
```sh
python manage.py runserver
```

## Authors
    👨‍🎓 Saparkhan Kassymbekov 
    👨‍🎓 Nurbek Malikov
    👩‍🎓 Akbayan Bekbossynova
    👨‍🎓 Kuanysh Akhmetzhanov

## License
_MIT License_
