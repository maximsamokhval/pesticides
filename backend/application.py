import logging
import os
from logging.handlers import RotatingFileHandler

import redis
import requests
from flask import Flask, render_template
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# todo для сборки в докер заменить 127.0.0.1 на redis
redis = redis.StrictRedis(host="redis", port=6379, decode_responses=True)

# Настройка логгера
logger = logging.getLogger("backend")
logger.setLevel(logging.INFO)
# Настройка логгера
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Создание и настройка обработчика с ротацией логов
log_file = "backend.log"
max_log_size = 1024 * 1024 * 4  # 4 МБ
backup_count = 5  # Количество ротированных файлов

handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=backup_count)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

ENDPOINT_LOGIN = os.environ.get("ENDPOINT_LOGIN", "")
ENDPOINT_PASSWORD = os.environ.get("ENDPOINT_PASSWORD", "")
API_AUTH = HTTPBasicAuth(ENDPOINT_LOGIN, ENDPOINT_PASSWORD)
ENDPOINT = os.environ.get("ENDPOINT", "http://vs-samokhval/active-substances/hs/pesticides/v1/status")

@app.route('/', methods=['GET'])
def main_page():

    # получение данных из кеша
    if redis.get('pesticides') is None:
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(
                url=ENDPOINT,
                auth=API_AUTH,
                headers=headers)

            redis.setex('pesticides', time=3600, value=response.text)
            JsonData = response.text

        except requests.exceptions.RequestException as e:
            print(f'{e}')
            logger.critical(f"Ошибка обращения к URI {ENDPOINT}\n {e}")
    else:
        JsonData = redis.get('pesticides')

    return render_template('index.html', jd=JsonData)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3300)
