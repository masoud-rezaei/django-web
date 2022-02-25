FROM python:alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/   
RUN apk update
RUN apk add --no-cache gcc python3-dev musl-dev
RUN pip install --upgrade pip 
RUN pip install  -r requirements.txt   
ADD . /code/
RUN pip install --system
EXPOSE 8000
CMD  python manage.py makemigrations --noinput && \
     python manage.py migrate --noinput &&\
     python manage.py collectstatic --noinput &&\
     python manage.py createsuperuser --user admin --email admin@localhost --noinput && \
     python manage.py runserver 0.0.0.0:8000  --noinput 
COPY . /code/