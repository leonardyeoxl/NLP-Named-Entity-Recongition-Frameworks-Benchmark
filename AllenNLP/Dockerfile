FROM python:3.7-slim

RUN apt-get update && apt-get install -y make g++ 

COPY requirements.txt .
RUN pip install -r requirements.txt