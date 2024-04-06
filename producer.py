import streamlit as st
from kafka import KafkaProducer
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

# Extract the broker addresses
# broker_addresses = [node.split(':')[0] for broker in cluster_metadata.brokers]

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Streamlit app
def main():
    st.title("Live Chat Room")

    # Get user input
    message = st.text_input("Enter your message")

    # Send message to Kafka topic
    if st.button("Send"):
        if message:
            data = {"message": message}
            producer.send('chat-topic', value=data)
            st.success("Message sent successfully!")
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()