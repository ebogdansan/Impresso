========================================
         IMPRESSO — Ghid de instalare
========================================

Sistem de gestiune pentru impresari si firme de management artistic.
Construit cu Django + MySQL.

----------------------------------------
CERINTE PREALABILE
----------------------------------------

- Python 3.x instalat
- MySQL Server 8.0 instalat si pornit
- MySQL Workbench (optional, pentru vizualizare BD)
- pip disponibil in terminal

----------------------------------------
PASUL 1 — Porneste MySQL Server
----------------------------------------

Din PowerShell ca Administrator:

    net start mysql

Sau din Windows Services (services.msc) → MySQL → Start.

----------------------------------------
PASUL 2 — Instaleaza dependentele
----------------------------------------

    pip install -r requirements.txt

----------------------------------------
PASUL 3 — Configureaza variabilele de mediu
----------------------------------------

Creaza un fisier .env in radacina proiectului cu urmatorul continut:

    SECRET_KEY=cheia_ta_secreta_din_settings.py (sau cheia pe care o primesti atunci cand instalezi django)
    DB_NAME=numele_bazei_de_date
    DB_USER=root
    DB_PASSWORD=parola_ta_mysql
    DB_HOST=localhost
    DB_PORT=3306

----------------------------------------
PASUL 4 — Importa baza de date (daca ai fisier .sql)
----------------------------------------

Deschide MySQL Workbench:
    1. Conecteaza-te la serverul local
    2. Server → Data Import
    3. Import from Self-Contained File → selecteaza fisierul .sql
    4. Default Target Schema → alege sau creeaza o schema
    5. Start Import

----------------------------------------
PASUL 5 — Ruleaza migratiile
----------------------------------------

    python manage.py migrate

----------------------------------------
PASUL 6 — Creeaza un superuser (administrator)
----------------------------------------

    python manage.py createsuperuser

Urmeaza instructiunile din terminal (username, email, parola).

----------------------------------------
PASUL 7 — Porneste serverul
----------------------------------------

    python manage.py runserver

Acceseaza aplicatia la:
    http://localhost:8000

Panoul de administrare la:
    http://localhost:8000/admin

----------------------------------------
TIPURI DE UTILIZATORI
----------------------------------------

  Standard     → poate vizualiza datele (read-only)
  Administrator → acces complet CRUD + Admin Panel

  Atentie: pentru a modifica date trebuie sa te autentifici
  ca administrator. Utilizatorii standard au acces doar de citire.

----------------------------------------
NOTE IMPORTANTE
----------------------------------------

- Fisierul .env NU este inclus in repository (motive de securitate).
  Trebuie creat manual la fiecare instalare noua.

- DEBUG=True este necesar in development pentru a incarca
  corect CSS-ul interfetei /admin. Nu folosi DEBUG=False local.

- Asigura-te ca MySQL Server este pornit inainte de
  a rula python manage.py runserver.

========================================