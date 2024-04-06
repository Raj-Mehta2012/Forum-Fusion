import streamlit as st
# from kafka import KafkaProducer
import json
from dotenv import load_dotenv
import os
# from confluent_kafka import admin
from confluent_kafka import Producer

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

# Create a Kafka producer
producer = Producer(props)

# Streamlit app
def main():
    st.title("Live Chat Room")

    # Get user input
    message = st.text_input("Enter your message")

    # Send message to Kafka topic
    if st.button("Send"):
        if message:
            data = {"message": message}
            producer.produce('chat-topic', value=json.dumps(data))
            producer.flush()
            st.success("Message sent successfully!")
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
