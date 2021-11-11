# pull official base image
FROM python:3.8.8-alpine

# set work directory
WORKDIR C:/Users/as/Desktop/apis/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .