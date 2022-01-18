FROM debian:10

RUN apt update
RUN apt install postgresql postgresql-contrib python-psycopg2 libpq-dev -y

USER postgres

RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker docker

USER root
RUN apt install python3-dev python3-pip nginx -y

ENV DB_TYPE=POSTGRES
ENV DEBUG=0

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 80
EXPOSE 5005

RUN chmod +x entrypoint.sh

COPY nginx_conf /etc/nginx/sites-enabled/default

CMD ["./entrypoint.sh"]
