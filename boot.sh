#!/bin/bash
# активируем виртуальную среду
source venv/bin/activate
# Повторные попытки подключения к базе данных каждые 5 секунд
while true; do
    # обновляем базу данных
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
# компилируем языковые переводы
flask translate compile
# запускаем сервер с помощью gunicorn
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app