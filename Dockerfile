FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

# dependencies for psycopg2-binary
RUN apk add --no-cache mariadb-connector-c-dev
# grpcio 설치를 위한...
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN apk add build-base linux-headers 
RUN apk add g++

RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base


# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# tts .json file
COPY dislodged-tts-project-11e592a89e01.json /app/dislodged-tts-project-11e592a89e01.json

# Now copy in our code, and run it
COPY . /app/