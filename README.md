# DS4A - IGAC (admin)

## Developers
### Setup
#### Virtual env
```
python -m venv .venv
```
#### Activate
```
source .venv/bin/activate
```

#### Install dependencies
```
pip install -r requirements.txt
```

### Run
```
gunicorn IGAC.wsgi -w4 -b 0.0.0.0:8000
```

### Migrations
#### First run
```
python manage.py migrate  # create django tables
python manage.py makemigrations persistance  # entries in models
python manage.py migrate --fake-initial
```

