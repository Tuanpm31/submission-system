### Run local server
`python manage.py makemigrations`

`python manage.py migrate`

###Run with docker
`docker build . -t submit-system-v0.0`

`docker run -p 8000:8000 submit-system-v0.0`