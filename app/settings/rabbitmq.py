import os, pika

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
rabbitmq = connection.channel()

