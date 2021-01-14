sudo docker rm b785318b8cbcc008b7cf82ac9ca83fa6ffffd3d901be8aee7932a8e3d0a86152
sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

