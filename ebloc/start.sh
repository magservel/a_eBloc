sudo docker rm 3dd103e7bf30044db7c8e3dcc911f9767cd3dd4b1e6404a24011b5f7c5d76356
sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver
