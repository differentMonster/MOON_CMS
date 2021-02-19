###########
# BUILDER #
###########

FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# nano install
RUN apt-get update
RUN apt-get install nano

# install dependencies
# copy using poetry.lock* in case it doesn't exist yet
COPY pyproject.toml poetry.lock* /

RUN poetry install --no-root

COPY . /opt/wedding_house_project/

# docker - copy all file
COPY . /opt/wedding_house_project/backend

# docker - webapp focus folder
WORKDIR /opt/wedding_house_project/backend

EXPOSE 8000
ENTRYPOINT ["/opt/wedding_house_project/backend/docker/dev/entrypoint.sh"]