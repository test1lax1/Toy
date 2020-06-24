# pull official base image
FROM python:3.7.4-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv env
RUN chmod 777 /env/bin/activate
RUN /env/bin/activate
RUN env/bin/pip install --upgrade pip

COPY ./requirements.txt .
RUN  /env/bin/pip install -r requirements.txt


WORKDIR /env
volume /env
EXPOSE 8080
COPY . /env

RUN chmod 777 /env/bin/activate

CMD /env/bin/activate
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
