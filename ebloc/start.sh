sudo docker rm 212913cb38cbaf1ccecb357544ad337b493b73971527f8473f4edf33a4b8c3f7
sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

