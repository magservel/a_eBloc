sudo docker rm 6924a91aba42aa6289ee557d062593bef8e87b4a7a78d4182e0a03579757ecb1
sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

