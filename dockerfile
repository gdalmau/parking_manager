FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /parking_manager

WORKDIR /parking_manager

ADD . /parking_manager/

RUN pip install -r requirements.txt

