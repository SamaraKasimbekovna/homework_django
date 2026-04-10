# 1 Активировать виртуальную среду
source myenv/bin/activate

# 2 Проводим фиксацию наших настроек
python manage.py migrate (изменение в настройках необходимо зафиксировать)

python manage.py makemigrations


# 3 Запустить сервер
python manage.py runserver

# 
python manage.py startapp (app_name (создание приложения)  

python manage.py createsuperuser (создание суперпользователя)         