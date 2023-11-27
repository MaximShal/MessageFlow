#!/bin/bash

until netcat -z -v -w30 rabbitmq 5672; do
  echo "Waiting for RabbitMQ to come up..."
  sleep 5
done

poetry run python main.py