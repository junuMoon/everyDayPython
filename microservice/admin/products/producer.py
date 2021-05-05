import pika
import json


params = pika.URLParameters('amqps://tuiedqst:IEoY_OrS1UQUjBYoUameCjfk0DSSB9HJ@dingo.rmq.cloudamqp.com/tuiedqst')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

    