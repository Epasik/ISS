#!/usr/bin/env python3
import logging

import connexion

from swagger_server import encoder
from prometheus_flask_exporter import PrometheusMetrics
from swagger_server.controllers import playlists_controller
from prometheus_flask_exporter import Gauge

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    metrics = PrometheusMetrics(app.app)
    # Добавляем счетчик для отслеживания количества запросов к эндпоинту /playlists
    metrics.info('playlists_info', 'Request Count', labels={'endpoint': '/playlists'})
    # Создаем гауговый счетчик для отслеживания количества плейлистов
    playlist_count_metric = Gauge('playlist_count2', 'Number of playlists')
    # Обновляем значение счетчика в соответствии с переменной count из playlists_controller
    playlist_count_metric.set_function(lambda: playlists_controller.playlist_count)

    logging.basicConfig(filename='./var/log/new.log', level=logging.INFO)

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Музыкальная бибилотека API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
