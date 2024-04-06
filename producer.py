import streamlit as st
from kafka import KafkaProducer
import json

#Replace this from GCP 
broker_addresses = ['RajTest123-kafka.REGION.gcp.confluent.cloud:9092']

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=broker_addresses,
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