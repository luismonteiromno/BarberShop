FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libmagic1 \
    libcairo2-dev \
    libgdk-pixbuf-xlib-2.0-dev \
    libglib2.0-dev \
    gir1.2-glib-2.0 \
    libpango1.0-dev \
    libxml2-dev \
    libxslt1-dev \
    libxmlsec1-dev \
    libxmlsec1-openssl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r requirements.txt 

COPY . /app/

RUN /env/bin/python manage.py collectstatic --noinput

EXPOSE 8000
EXPOSE 5678
