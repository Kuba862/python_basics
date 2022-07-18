FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /projectApp
COPY requirements.txt /projectApp/
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -r requirements.txt
COPY . /projectApp/