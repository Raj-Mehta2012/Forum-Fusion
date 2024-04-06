# Use the official lightweight Python image
FROM python:3.9-slim

# Copy the application code
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "producer.py"]