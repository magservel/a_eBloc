sudo docker rm 3553e1294019d0ee18a324b41bdf50c923bbbd5119c50f66e9f201d9e98950d3
sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver
