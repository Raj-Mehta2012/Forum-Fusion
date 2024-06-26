# Forum Fusion

Forum Fusion is a live chat platform leveraging Confluent Kafka for real-time data streaming and messaging, ensuring seamless user interactions. The application features a Streamlit-based frontend for dynamic user engagement, containerized with Docker for consistency, and deployed on Google Kubernetes Engine for robust scalability and manageability.

## Introduction

Forum Fusion is designed to provide a Reddit-like live chat experience with real-time data streaming. Utilizing Confluent Kafka, Streamlit, Docker, and Google Kubernetes Engine, it ensures efficient data processing and interactive user engagement.

## Tech Stack

- **Backend**: Python, Kafka
- **Frontend**: Streamlit
- **Containerization**: Docker
- **Orchestration and Deployment**: Google Kubernetes Engine (GKE)

## Prerequisites

1. Set up a GCP account: [Google Cloud Platform](https://cloud.google.com/)
2. Create a Kafka cluster in GCP:
   - Go to the "Artificial Intelligence" section in the GCP Console
   - Select "Dataproc" and then "Clusters"
   - Click "Create Cluster" and choose "Kafka" as the component
   - Configure the cluster according to your requirements
3. Install the following Python libraries:
   ```bash
   pip3 install kafka-python streamlit
   ```

## Architecture Diagram

graph LR
    A[Producer (Streamlit)] -->|Messages| B[Apache Kafka Cluster (GCP)]
    B -->|Messages| C[Consumer (Real-time chat view)]
    D[Docker Container] -->|Contains| E[Producer and Consumer Apps]
    E -->|Deploy| F[Google Kubernetes Engine (GCP)]

## Building the Producer

1. Create a separate Python application that produces messages to the Kafka cluster.
2. Use the Kafka Python client to publish messages to the appropriate topic.
3. Implement a Streamlit-based UI for real-time chat input and display.

## Building the Consumer

1. Create a separate Python application that consumes messages from the Kafka cluster.
2. Use the Kafka Python client to subscribe to the appropriate topic.
3. Implement a real-time display of received messages (e.g., using Streamlit or another UI framework).

## Testing the Application Locally

1. Start the Kafka cluster locally (e.g., using Docker or a local Kafka installation).
2. Run the Producer (Streamlit app) and the Consumer applications.
3. Test sending messages from the Streamlit app and verify that they're displayed in the Consumer.

## Deploying to GCP

1. Package your Producer and Consumer applications into Docker containers.
2. Push the Docker images to Google Container Registry.
3. Deploy the Producer (Streamlit app) and Consumer applications to Google Kubernetes Engine.
4. Configure the applications to connect to the Cloud Kafka cluster.

## Useful Links

- [Google Cloud Kafka documentation](https://cloud.google.com/kafka)
- [Kafka Python client documentation](https://kafka-python.readthedocs.io/)
- [Streamlit documentation](https://docs.streamlit.io/)
- [GCP App Engine documentation](https://cloud.google.com/appengine)
- [GCP Cloud Run documentation](https://cloud.google.com/run)
- [GCP Kubernetes Engine documentation](https://cloud.google.com/kubernetes-engine)
