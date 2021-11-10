FROM python:3.7-buster

ENV PYTHONUNBUFFERED=1

# install nginx
COPY install-nginx.sh /
RUN bash /install-nginx.sh
EXPOSE 80

# copy nginx config
COPY nginx/uwsgi_params /etc/nginx/uwsgi_params
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/dhost.conf /etc/nginx/conf.d/default.conf

# create source code folder
RUN mkdir -p /var/www/code
WORKDIR /var/www/code

# install logrotate, odbc dependencies
RUN apt-get update \
    && apt-get install -y gcc logrotate \
    && apt-get install -y gettext \
    && apt-get install -y redis-server

# clean the install
RUN apt-get -y clean

# install dependencies
COPY src/requirements.txt /var/www/code/
RUN pip install -r requirements.txt

# uwsgi & logrotate config
COPY uwsgi/logrotate /etc/logrotate.d/dmp
COPY uwsgi/uwsgi.ini /etc/uwsgi/uwsgi.ini

# copy soruce code
COPY src /var/www/code/
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "sh", "/entrypoint.sh" ]