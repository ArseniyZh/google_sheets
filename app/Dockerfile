FROM python:latest

WORKDIR /usr/app/src

COPY . .


RUN apt-get update -y && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]