# start by pulling the python image
FROM python:3.11-slim

LABEL authors="samokhval"
WORKDIR /backend

# Copy all files to the working directory
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install the dependencies and packages in the requirements file
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt
