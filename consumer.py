from kafka import KafkaConsumer
import json

# Change This
broker_addresses = ['RajTest123-kafka.REGION.gcp.confluent.cloud:9092']

# Create a Kafka consumer
consumer = KafkaConsumer('chat-topic',
                         bootstrap_servers=broker_addresses,
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