FROM python:3.12

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


WORKDIR /django-app

COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .
EXPOSE 1111
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
