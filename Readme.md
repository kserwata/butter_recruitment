# Butter recruitment task

Application for processing activities data. It allow access for data using REST API.
It's done using Django and DRF.

## Importing data

Just call endpoint `/api/activites/import/` with data as json body with POST request.

## Aggregate data 

Just call endpoint `/api/activities/aggregate` as GET request. Param `track_id` is required.

# Running application

Build docker image:
```bash
docker build -t butter_recruitment .
```

Running container:
```bash
docker run -p 80:8080 -d butter_recruitment 
```

Application will be available by typing `http://localhost:8080` in Your browser.

# Testing

For testing, You need to:
- install all requirements, make local DB using `python manage.py migrate`
- spin local server using `python manage.py runserver`
- run tests using `python manage.py test`