# DS4A - IGAC (admin)

## Developers
### Setup
#### Create a virtual env
```
python -m venv .venv
```
#### Activate it
```
source .venv/bin/activate
```

#### Install dependencies
```
pip install -r requirements.txt
```

### Modify .env
A `.env` must containg the environmental variables required for accesing DB. 
An example of the variables required is shown in `example.env`. Copy the example file as .env and fill in the credentials
```
cp IGAC/example.env IGAC/.env
nano IGAC/.env
```

### Run
```
cd IGAC
gunicorn IGAC.wsgi -w4 -b 0.0.0.0:8000
```

### Migrations (Only needed if DB is new)
#### First run
```
python manage.py migrate  # create django tables
python manage.py makemigrations persistance  # entries in models
python manage.py migrate --fake-initial
```

### Modify columns on db
```
ALTER TABLE coordenadas DROP COLUMN index;
ALTER TABLE coordenadas ADD COLUMN index SERIAL PRIMARY KEY;
ALTER TABLE bdl_detallada_filtrada DROP COLUMN index;
ALTER TABLE bdl_detallada_filtrada ADD COLUMN index SERIAL PRIMARY KEY;
```
