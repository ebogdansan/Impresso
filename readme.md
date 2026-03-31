# Impresso 🎵

**Database management system for talent agencies and artist management companies.**

Impresso is a Django-based web application designed to help talent managers and agencies efficiently manage their artists and the groups they represent.

---

## Features

- **Group management** — add, edit and delete groups from your portfolio
- **Member management** — manage individual members within each group
- **Association table** — link members to groups with detailed info: role, join date, activity status
- **Role-based authentication** — standard users (read-only) and administrators (full CRUD access)
- **Admin panel** — Django Admin interface for quick data management
- **Full CRUD** — Create, Read, Update, Delete across all entities

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** MySQL
- **Connector:** `mysqlclient`
- **Authentication:** Django Authentication (standard users + superuser)
- **Configuration:** `python-decouple` for environment variables

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/ebogdansan/impresso.git
cd impresso
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the project root:
```
SECRET_KEY=your_secret_key_from_settings.py (or the key generated when you install Django)
DB_NAME=your_database_name
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 4. Import the database (if you have a .sql file)

Open MySQL Workbench:
1. Connect to the local server
2. **Server → Data Import**
3. Import from Self-Contained File → select your `.sql` file
4. Default Target Schema → choose or create a schema
5. **Start Import**

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Start the server
```bash
python manage.py runserver
```

Access the application at `http://localhost:8000` , or any other port if port 8000 is taken.

---

## User Types

| Type | Access |
|------|--------|
| **Standard** | View data (read-only) |
| **Administrator** | Full CRUD access + Admin Panel |

---

## Project Structure

```
impresso/
├── manage.py
├── .env               # environment variables (not included in repo)
├── .gitignore
├── requirements.txt
└── django_crud/
    ├── settings.py
    ├── urls.py
    └── ...
```

---

## Notes

- The `.env` file is not included in the repository for security reasons. It must be created manually on each new installation.
- Make sure MySQL Server is running before starting the application (`net start mysql` in PowerShell as Administrator).
- `DEBUG=True` is required in development for the `/admin` interface to load CSS correctly. Do not use `DEBUG=False` locally.
