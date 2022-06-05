# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
MAINTAINER Inga Sokolova

RUN apt-get update -y

COPY . .
WORKDIR .
RUN apt install -y python3-pip
RUN pip3 install --trusted-host files.pythonhosted.org -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]