"""
Angel Rodriguez

Final Project

A command line python program that sends and receives encrypted information using RabbitMQ
and Diffie-Hellman key exchange ideas.

27 November 2018
"""

#!/usr/bin/env python
import pika

#establish connection to the server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#agree on a modulus and base for both parties, which can be seen for everyone, but the secret integer is kept to each and not shares
modulus = 23
base = 5
secret = 4

print("Agreed on modulus: " + str(modulus) + "\nand base: " + str(base))

#Diffie-Hellman
key = base ** secret % modulus
print(key)


channel.queue_declare(queue='hello')

#send the message, which in this case would be the "key"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(key))

print(" [x] Sent message.")
connection.close()
