# LiveChatRoom
 
 ## Pre-Requisites:

 1. Set-up GCP account : https://cloud.google.com/
 2. Create Kafka cluster in GCP: Go to 
 "Artificial Intelligence" section in the GCP Console -> Select "Dataproc" and then "Clusters" -> Click "Create Cluster" and choose "Kafka" as the component -> Configure the cluster according to your requirements
 3. Install following pyhon3 libraries
 ```pip3 install kafka-python streamlit```  

 ## Architecture Diagram:

 ┌──────────────┐            ┌───────────────┐
│   Producer   │            │               │
│  (Streamlit) │            │    Apache     │
│              ├──────────▶┤   Kafka       │
└──────────────┘            │   Cluster     │
                            │    (GCP)      │
                            │               │
                            └───────┬───────┘
                                    │
                                    │
                            ┌───────▼───────┐
                            │   Consumer    │
                            │ (Real-time    │
                            │  chat view)   │
                            └───────────────┘

## Building the Producer:

1. Create a separate Python application that consumes messages from the Kafka cluster.
2. Use the Kafka Python client to subscribe to the appropriate topic.
3. Implement a real-time display of received messages (e.g., using a terminal or a simple GUI).

## Building the Consumer:

1. Create a separate Python application that consumes messages from the Kafka cluster.
2. Use the Kafka Python client to subscribe to the appropriate topic.
3. Implement a real-time display of received messages (e.g., using a terminal or a simple GUI).


## Test the application locally

1. Start the Kafka cluster locally (e.g., using Docker or a local Kafka installation).
2. Run the Producer (Streamlit app) and the Consumer applications.
3. Test sending messages from the Streamlit app and verify that they're displayed in the Consumer.

## Deploy to GCP

1. Package your Producer and Consumer applications.
2. Deploy the Producer (Streamlit app) to a GCP service like App Engine or Cloud Run.
3. Deploy the Consumer application to a GCP service like Cloud Run or Kubernetes Engine.
4. Configure the applications to connect to the Cloud Kafka cluster.

## Useful links:

Google Cloud Kafka documentation: https://cloud.google.com/kafka
Kafka Python client documentation: https://kafka-python.readthedocs.io/
Streamlit documentation: https://docs.streamlit.io/
GCP App Engine documentation: https://cloud.google.com/appengine
GCP Cloud Run documentation: https://cloud.google.com/run
GCP Kubernetes Engine documentation: https://cloud.google.com/kubernetes-engine
