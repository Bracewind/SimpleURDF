FROM python:latest

RUN apt-get install gcc

# activate venv
ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

RUN pip install poetry

COPY . /home/project
WORKDIR /home/project
RUN poetry install
ENTRYPOINT ["tail", "-f", "/dev/null"]
