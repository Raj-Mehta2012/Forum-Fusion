import streamlit as st
from kafka import KafkaConsumer
import json
from dotenv import load_dotenv
import os
from confluent_kafka import admin

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
    'sasl.password': api_secret
}

# Create a Kafka admin client
admin_client = admin.AdminClient(props)

# Get the cluster metadata
cluster_metadata = admin_client.list_topics(timeout=10)

# # Extract the broker addresses
# broker_addresses = [node.split(':')[0] for broker in cluster_metadata.brokers]

# Create a Kafka consumer
consumer = KafkaConsumer('chat-topic',
                         bootstrap_servers=bootstrap,
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Function to print received messages
def print_message(message):
    print(f"Received message: {message['message']}")

# Consume messages from Kafka
print("Listening for messages...")
for message in consumer:
    message_data = message.value
    print_message(message_data)

# Clean up the consumer
consumer.close()