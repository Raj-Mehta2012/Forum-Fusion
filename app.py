import os
from confluent_kafka import Producer, Consumer, KafkaException, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Kafka configuration
config = {
    'bootstrap.servers': os.getenv('CONFLUENT_CLUSTER'),
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': os.getenv('CONFLUENT_KEY'),
    'sasl.password': os.getenv('CONFLUENT_SECRET'),
    'group.id': 'streamlit-reddit-group',
    'auto.offset.reset': 'earliest',
    'debug': 'generic,broker,security'  # Enables detailed debug logging
}


# Initialize Kafka Admin Client
admin_client = AdminClient({'bootstrap.servers': config['bootstrap.servers']})

def create_topic(topic_name):
    try:
        st.write(f"Attempting to create topic {topic_name}...")
        topic_list = [NewTopic(topic_name, num_partitions=1, replication_factor=1)]
        admin_client.create_topics(topic_list)
        st.write("Topic created successfully.")
    except Exception as e:
        st.error(f"Failed to create topic due to error: {e}")


def get_topics():
    try:
        admin_config = {
          "bootstrap.servers": os.getenv('CONFLUENT_CLUSTER'),
          "security.protocol": "SASL_SSL",
          "sasl.mechanisms": "PLAIN",
          "sasl.username": os.getenv('CONFLUENT_KEY'),
          "sasl.password": os.getenv('CONFLUENT_SECRET'),
      }
        admin_client = AdminClient(admin_config)

        # Get list of existing topics
        existing_topics = admin_client.list_topics().topics
        return [topic for topic in existing_topics]
    except Exception as e:
        st.error(f"Failed to fetch topics due to error: {e}")
        return []

def kafka_producer():
    return Producer(config)

def kafka_consumer(topics):
    st.write(f"Subscribing to topics: {topics}")
    consumer = Consumer(config)
    consumer.subscribe(topics)
    return consumer

def produce_message(topic, message):
    producer = kafka_producer()
    try:
        st.write(f"Sending message to topic {topic}: {message}")
        producer.produce(topic, value=message.encode('utf-8'))
        producer.flush()
        st.write("Message sent successfully.")
    except Exception as e:
        st.error(f"Failed to send message due to error: {e}")

def consume_messages(consumer, max_messages=1000):
    messages = []
    try:
        for _ in range(max_messages):  # Limit the number of messages to prevent infinite loops
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                # st.write("No new messages.")
                continue
            if msg.error():
                st.error(f"Consumer error: {msg.error()}")
                continue
            message_value = msg.value().decode("utf-8")
            st.write(f"Received message: {message_value}")
    finally:
        consumer.close()
        st.write("Consumer closed.")
    return messages

# Streamlit UI components
st.title('Reddit-like Messaging Board')
all_topics = get_topics()
if st.button("Refresh Topics"):
    all_topics = get_topics()
topic = st.selectbox('Choose a topic or create a new one', options=all_topics + ["Create new topic..."])

if topic == "Create new topic...":
    new_topic_name = st.text_input("Enter new topic name")
    if st.button("Create Topic"):
        create_topic(new_topic_name)
        all_topics = get_topics()  # Refresh topic list
elif topic:
    message = st.text_area("Message")
    if st.button("Send"):
        produce_message(topic, message)
    if st.button("Load Messages"):
        consumer = kafka_consumer([topic])
        messages = consume_messages(consumer)
        st.write("Messages in topic:", messages)

