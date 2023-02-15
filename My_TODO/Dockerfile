from python:3.10.6

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y libpq-dev
RUN apt-get install -y postgresql
RUN apt-get install -y postgresql-contrib

RUN apt-get install -y python3-dev

RUN pip3 install --upgrade pip

COPY ./my_TODO/ ./
RUN pip3 install -r requirements.txt

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh
RUN pip3 install gunicorn