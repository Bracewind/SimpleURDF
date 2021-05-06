FROM python:latest

RUN apt-get install gcc

# activate venv
ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

RUN pip install poetry
RUN pip install pytest

