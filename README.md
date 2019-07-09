# Development Environment Setup

## Getting started dependencies

This dependencies are necessary to follow this tutorial

#### Python

Probably you already have python installed. You should use the 3.x version. You can check it executing

```bash
python --version
```

#### Python dependencies and Local Virtual Environment


Install pip if it is not installed

bash
```bash
sudo apt-get install python-pip
```

mac os
```mac os
sudo easy_install python-pip
```

We assume you have python 3.x installed (refer to section Getting started dependencies).

bash
```bash
sudo apt install virtualenv 
```

mac os
```mac os
sudo pip install virtualenv
```
***Requirements***

The backend uses some libraries which are detailed in requirements.txt, in order to install them execute the following commands (you must be in the directory where this README is in):

```bash
virtualenv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```

## Start Project

#### Making migrations

```bash
python manage.py makemigrations notebook
```

```bash
python manage.py migrate notebook
```

#### Start

```bash
python manage.py runserver
```