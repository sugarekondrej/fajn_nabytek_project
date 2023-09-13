FROM python:latest

RUN mkdir /srv/app
WORKDIR /srv/app
ADD * .
RUN pip install -r requirements.txt
