sudo docker rm 2b4c6baa080764330ee12feb8fd948ed55018dab38f34932861dcbb8a956b1b8
sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver

