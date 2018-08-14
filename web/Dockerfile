FROM python:3.6-alpine

ENV APP_HOME=/app myvar=123


LABEL MAINTAINER="Alejandro Madrazo" EMAIL="amadrazo@ufm.edu"
WORKDIR ${APP_HOME}

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt


# COPY src dest
COPY hello.py ${APP_HOME}/


CMD ["python" ,"./hello.py"]
EXPOSE 5000