from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic
import time
import streamlit as st
import json
from dotenv import load_dotenv
import os

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

# Create an admin client
admin_client = AdminClient(props)

# Create the topic
topic_name = 'chat-topic'
topic_list = []
topic_list.append(NewTopic(topic_name, num_partitions=1, replication_factor=3))

# Call create_topics to create the topic
created_topics = admin_client.create_topics(new_topics=topic_list)

# Wait for the topic creation to complete
for topic, future in created_topics.items():
    try:
        future.result()  # Wait for the Future to complete
        print(f"Topic {topic} created successfully")
    except Exception as e:
        print(f"Error creating topic {topic}: {e}")

# # Close the admin client
# admin_client.