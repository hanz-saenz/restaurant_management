FROM ubuntu:22.04

ENV LAST_UPDATED 2024-02-05
# Hace update antes de iniciar
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update

# Instala los paquetes requeridos
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y -u python3 curl ghostscript imagemagick openssh-server wget libpcap-dev libpq-dev python3-dev python3-setuptools git-core python3-pip build-essential rabbitmq-server graphviz graphviz-dev libmagickwand-dev poppler-utils tesseract-ocr tesseract-ocr-spa ffmpeg unzip xvfb wkhtmltopdf cron

# ADD deploy.sh deploy.sh
RUN ls
# Instala los requerimientos de docker desde deploy.sh
# RUN DEBIAN_FRONTEND=noninteractive sh deploy.sh requirements-docker

#upgrade de pip
RUN  pip3 install setuptools --upgrade
#RUN pip3 install --upgrade pip

#fix bug simplejson
RUN pip3 install django-realtime --upgrade
RUN apt-get update -y
RUN apt-get install -y tzdata

ENV  LC_ALL=C.UTF-8
ENV  LANG=C.UTF-8
ENV TZ America/Bogota
#Instala los requirementos
ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --ignore-installed

RUN pip3 install psycopg2-binary==2.8.6

#define el directorio de trabajo
WORKDIR /restaurant_management