sudo docker rm a276578d487d9480e1792194e28dc35ac1b9410d7f436473bd14640d0a160899
sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver

