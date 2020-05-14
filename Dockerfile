# mypaas.service = pyzo.org
#
# mypaas.url = https://pyzo.org
# mypaas.url = https://www.pyzo.org
# mypaas.url = https://community.pyzo.org
# mypaas.url = https://repo.pyzo.org
# mypaas.url = https://issues.pyzo.org
# mypaas.url = https://guide.pyzo.org
# mypaas.url = https://miniconda.pyzo.org
# mypaas.url = https://matlab.pyzo.org
#
# mypaas.scale = 0
# mypaas.maxmem = 256m

FROM python:3.8-slim-buster

RUN apt update \
    && pip --no-cache-dir install pip --upgrade \
    && pip --no-cache-dir install uvicorn uvloop httptools \
    && pip --no-cache-dir install markdown pygments asgineer==0.7.1

WORKDIR /root
COPY . .
CMD ["python", "server.py"]
