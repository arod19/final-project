"""
Angel Rodriguez

Final Project

A command line python program that sends and receives encrypted information using RabbitMQ
and Diffie-Hellman key exchange ideas.

27 November 2018
"""

#!/usr/bin/env python
import pika

#establish a connection to the server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#agree on a same modulus and base.
modulus = 23
base = 5
secret = 3

print("Agreed on modulus: " + str(modulus) + "\nand base: " + str(base))

#Diffie-Hellman
key = base ** secret % modulus
print(key)



channel.queue_declare(queue='hello')

#receive the body from the sender
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

#decrypt using Diffie-Hellman
    decrypted = int(body.decode("utf-8")) ** secret % modulus
    print(decrypted)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
