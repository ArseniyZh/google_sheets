FROM python:latest

WORKDIR /usr/app/src

COPY main.py ./
COPY google_sheets_api.py ./
COPY commands/commands.py ./
COPY course/course_translation.py ./
COPY database/database.py ./
COPY telegram_messages/bot.py ./
COPY credentials.json ./

RUN apt-get update -y && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]