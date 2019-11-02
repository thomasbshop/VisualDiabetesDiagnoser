# pull official base image
FROM python:3.6-alpine

# set environment variables
ENV FLASK_APP visual_diagnoser.py
ENV FLASK_CONFIG production

RUN adduser -D visual_diagnoser
USER visual_diagnoser

WORKDIR /home/visual_diagnoser

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY visual_diagnoser.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
