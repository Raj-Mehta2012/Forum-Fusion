#!/bin/bash

export PORT=8080
streamlit run producer.py --server.port=$PORT

# EXPOSE 8080


