# Phone Book Management System

A simple contact manager built with Django 5.2 and MySQL. It supports adding, listing, searching, viewing, editing, and deleting contacts. No user login is required.

## Requirements
- Windows 10/11
- Python 3.10–3.13 recommended
- MySQL Server or XAMPP MariaDB/MySQL
- Internet connection for Bootstrap CDN styling

## 1. Create the database
Start MySQL in XAMPP (or start your MySQL service), then open phpMyAdmin or MySQL Workbench and run:

```sql
CREATE DATABASE phonebook_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

If `phonebook_db` already exists, you can use it; do not create it again.

## 2. Open the project
Extract the ZIP, then open PowerShell in the `phonebook_management_system` folder (the folder containing `manage.py`).

## 3. Create and activate a virtual environment
```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, run this once in the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## 4. Install packages
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`mysqlclient` needs a compatible wheel/build environment on some Windows setups. If installation fails, use Python 3.12 (64-bit) and upgrade pip first. Do not randomly install multiple MySQL drivers; the supplied project uses `mysqlclient`.

## 5. Configure database credentials
The defaults in `phonebook/settings.py` are:
- database: `phonebook_db`
- username: `root`
- password: blank
- host: `127.0.0.1`
- port: `3306`

These defaults suit a typical local XAMPP installation with an empty root password. If your MySQL account has a password, set it in PowerShell before running Django:
```powershell
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
$env:DB_NAME="phonebook_db"
```
Use the actual username and password configured in your database server. Do not expose database credentials publicly.

## 6. Create the tables
```powershell
python manage.py makemigrations contacts
python manage.py migrate
```

## 7. Run the website
```powershell
python manage.py runserver
```
Open http://127.0.0.1:8000/ in your browser.

## 8. Use the phone book
- Click **Add Contact** to save a person.
- Use the search field to find contacts by first name, last name, phone number, or email.
- Open a contact to view full details.
- Use **Edit** to update a contact.
- Use **Delete** to remove a contact.
- Phone numbers must be unique.

## Project structure
```text
phonebook_management_system/
├── manage.py
├── requirements.txt
├── README.md
├── phonebook/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── contacts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── __init__.py
    └── templates/
        └── contacts/
            ├── base.html
            ├── contact_list.html
            ├── contact_form.html
            ├── contact_detail.html
            └── contact_confirm_delete.html
```

## Troubleshooting
### MySQL connection refused / can't connect
1. Make sure the database service is running.
2. Check that MySQL is listening on port `3306`.
3. If XAMPP says port 3306 is in use, another MySQL/MariaDB service may already own it. Use only one database server, or configure the project to use the port of the server you actually started.
4. Confirm DB_HOST, DB_PORT, DB_USER, and DB_PASSWORD.

### Access denied for root
The password in Django must match the password for the MySQL account. Test logging in through MySQL Workbench/phpMyAdmin first.

### `No module named MySQLdb`
Activate the virtual environment and run:
```powershell
pip install mysqlclient
```

### Template or URL errors
Run commands from the folder containing `manage.py`, with the virtual environment activated.

## Before public deployment
This project is configured for local development (`DEBUG=True`). Before putting it on the internet, set `DEBUG=False`, use a strong secret key, configure `ALLOWED_HOSTS`, use a dedicated database account with limited privileges, enable HTTPS, and add authentication/access controls if the contact list should not be public. Anyone who can reach this no-login website can view and change its contacts.
