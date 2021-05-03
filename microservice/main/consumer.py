import pika
from pika import connection


params = pika.URLParameters('amqps://tuiedqst:IEoY_OrS1UQUjBYoUameCjfk0DSSB9HJ@dingo.rmq.cloudamqp.com/tuiedqst')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()