# IPL Data Analysis Django Project

A Django web application for analyzing and visualizing Indian Premier League (IPL) cricket data. The project provides interactive charts and statistics such as matches per year, matches won per team, extra runs conceded, and top economical bowlers, using data from CSV files.

## Features

- Visualizes IPL statistics with interactive charts (Highcharts)
- Imports and processes IPL data from CSV files
- Django models for matches and deliveries
- Custom management command for data import
- Modular app structure

## Folder Structure

```
├── db.sqlite3 # ignore this file in version control
├── manage.py
├── ReadMe.md
├── requirements.txt
├── data/
│   ├── deliveries.csv
│   └── matches.csv
├── django/                # Python virtual environment (not tracked by git)
│   └── ...
├── ipl_project/           # Django project settings and URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ipl_project_app/       # Main Django app (models, views, templates, static)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── management/
│   │   └── commands/
│   │       └── import_ipl_data.py
│   ├── migrations/
│   │   └── ...
│   ├── static/
│   │   ├── matches_per_year.js
│   │   ├── matches_won_per_team_per_year.js
│   │   ├── extra_runs_conceded_per_team_in_2016.js
│   │   └── top_10_economical_bowlers_in_2015.js
│   └── templates/
│       ├── index.html
│       ├── matches_per_year.html
│       ├── matches_won_per_team_per_year.html
│       ├── extra_runs_conceded_per_team_in_2016.html
│       └── top_10_economical_bowlers_in_2015.html
```

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:BhaskarAnil/django_ipl_project.git
cd django_ipl_project
```

### 2. Set Up Python Environment

It is recommended to use a virtual environment:

```bash
python3 -m venv django
source django/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the Database

Run migrations:

```bash
python manage.py migrate
```

### 5. Import IPL Data

Place `matches.csv` and `deliveries.csv` in the `data/` folder. Then run:

```bash
python manage.py import_ipl_data
```

This will populate the database with IPL match and delivery data.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure Details

### Models

- **Match**: Stores match-level data (season, teams, winner, etc.)
- **Delivery**: Stores ball-by-ball delivery data (bowler, batsman, runs, etc.)

### Management Commands

- `import_ipl_data.py`: Custom command to import data from CSV files into the database.

### Views & URLs

- Views in `ipl_project_app/views.py` process data and render templates with chart data.
- URLs are defined in `ipl_project_app/urls.py` and included in the main `ipl_project/urls.py`.

#### Example URLs

- `/` : Home page
- `/matches-per-year-chart/` : Matches played per year
- `/matches-won-per-team-per-year/` : Matches won per team per year
- `/extra-runs-conceded-per-team-in-2016/` : Extra runs conceded per team in 2016
- `/top-10-economical-bowlers-in-2015/` : Top 10 economical bowlers in 2015

### Templates & Static Files

- HTML templates are in `ipl_project_app/templates/`
- JavaScript for charts is in `ipl_project_app/static/`

## Notes

- The project uses SQLite by default for simplicity.
- Static files are served from the `static/` directory in development.
- For production, configure `STATIC_ROOT` and use `collectstatic`.


