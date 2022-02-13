FROM python:alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/     
RUN pip install  -r requirements.txt   
ADD . /code/
RUN pipenv install --system
EXPOSE 8000
CMD  python manage.py makemigrations --noinput && \
     python manage.py migrate --noinput &&\
     python manage.py collectstatic --noinput &&\
     python manage.py createsuperuser --user admin --email admin@localhost --noinput && \
     python manage.py runserver 0.0.0.0:8000  --noinput 
COPY . /code/