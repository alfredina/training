FROM ubuntu:latest
MAINTAINER Alfred Dushime  "alfredina01@gmail.com"
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install Flask
RUN pip install requests
EXPOSE 5001

