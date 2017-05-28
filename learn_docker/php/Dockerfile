FROM php:latest
RUN mkdir /root/project_prod
PROJECT_ROOT = $(pwd project_prod) 

COPY project_file /root/project_prod
WORKDIR $PROJECT_ROOT
RUN apt-get update
EXPOSE 80
