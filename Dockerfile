# Pull base image
FROM python:3.7-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/restaurant_ratings

# Install psycopg2
RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev && apk add postgresql-dev
RUN apk add --no-cache bash

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/restaurant_ratings/requirements.txt
RUN pip install -r requirements.txt

# Remove build-deps for size
RUN apk del build-deps

# Copy entrypoint
COPY ./entrypoint.sh /usr/src/restaurant_ratings/entrypoint.sh

# Copy project
COPY . /usr/src/restaurant_ratings

# Run entrypoint
ENTRYPOINT ["/usr/src/restaurant_ratings/entrypoint.sh"]
