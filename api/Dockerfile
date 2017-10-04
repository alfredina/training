FROM ubuntu:latest
MAINTAINER Alfred Dushime  "alfredina01@gmail.com"
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential mysql-client
COPY . /app
WORKDIR /app
RUN pip install Flask
RUN pip install pymysql
RUN apt-get install -y  freetds-dev
RUN apt-get install -y  iputils-ping
RUN pip install pymssql
RUN pip install flask-jsonpify
RUN pip install simplejson
EXPOSE 5001

