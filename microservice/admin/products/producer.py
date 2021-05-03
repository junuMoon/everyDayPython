import pika
from pika import connection


params = pika.URLParameters('amqps://tuiedqst:IEoY_OrS1UQUjBYoUameCjfk0DSSB9HJ@dingo.rmq.cloudamqp.com/tuiedqst')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')

    