import streamlit as st
import json
from dotenv import load_dotenv
import os
from confluent_kafka import Consumer, KafkaError
import json

# Load environment variables from .env file
load_dotenv()

bootstrap = os.getenv('CONFLUENT_CLUSTER')
api_key = os.getenv('CONFLUENT_KEY')
api_secret = os.getenv('CONFLUENT_SECRET')

# Connect to the Confluent Kafka cluster
props = {
    'bootstrap.servers': bootstrap,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': api_key,
    'sasl.password': api_secret,
    'group.id': 'chat-group',
    'auto.offset.reset': 'earliest'
}


# Create a Kafka consumer
consumer = Consumer(props)

# Subscribe to the chat topic
topic = 'chat-topic'
consumer.subscribe([topic])

# Function to print received messages
def print_message(message):
    value = message.value().decode('utf-8')
    message_data = json.loads(value)
    print(f"Received message: {message_data['message']}")

# Consume messages from Kafka
print("Listening for messages...")
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
        else:
            print_message(msg)

except KeyboardInterrupt:
    pass

finally:
    # Clean up the consumer
    consumer.close()