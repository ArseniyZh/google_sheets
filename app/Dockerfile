FROM python:latest

WORKDIR /usr/app/src

COPY app/main.py ./
COPY app/google_api/google_sheets_api.py ./
COPY app/commands/commands.py ./
COPY app/course/course_translation.py ./
COPY app/database/database.py ./
COPY app/telegram_messages/bot.py ./
COPY app/google_api/credentials.json ./
COPY app/config/config.py ./


RUN apt-get update -y && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]