# backend

Instalar django
    - pip instal django==2.1.15

Iniciar projeto e app
    - django-admin starproject enquetes .
    - django-admin startapp times

Criar models.py
    - Base
    - Time

Criar TimeAdmin no admin.py

Fazer migracções
    - manage.py makemigrations
    - manage.py migrate

Criar superusuario
    - manage.py createsuperuser

Rodar servidor e executar alguns cadastros em localhost:8000/admin
    - manage.py runserver

Instalar Django Rest Framework
    - pip install djangorestframework

Serializar class Time
    - criar serializers.py
    - serializar class Time

Criar rotas no projeto e no app
    - criar rota em enquete/urls.py
    - criar rota em times/urls.py
