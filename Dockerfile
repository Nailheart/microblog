# python:slim - образ контейнера, содержащий минимальный набор пакетов
# необходимых для запуска интерпретатора Python.
FROM python:slim

# создаем пользователя с именем microblog
RUN useradd microblog

# каталог по умолчанию, в который будет установлено приложение
WORKDIR /home/microblog

# копируем файл requirements.txt 
COPY requirements.txt requirements.txt
# создаем виртуальную среду
RUN python -m venv venv
# устанавливаем зависимости
RUN venv/bin/pip install -r requirements.txt
# установка дополнительных зависимостей
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
# chmod - гарантирует, что файл boot.sh будет установлен как исполняемый файл
RUN chmod a+x boot.sh

# установка переменной среды внутри контейнера
ENV FLASK_APP microblog.py

# устанавливаем владельца всех каталогов и файлов, которые были сохранены в /home/microblog,
# в качестве нового microblog пользователя
RUN chown -R microblog:microblog ./
# Меняем пользователя по умолчанию для всех команд на microblog пользователя
USER microblog

# порт сервера
EXPOSE 5000
# при запуске контейнера выполняем команды из файла boot.sh
ENTRYPOINT ["./boot.sh"]
