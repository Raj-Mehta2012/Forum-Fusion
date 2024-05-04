# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Set environment variables from .env file
ENV $(cat .env | xargs)

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]

# FROM python:3.8-slim

# WORKDIR /app

# ENV HOST 0.0.0.0

# COPY . /app
# COPY .env /app/.env

# RUN pip install --no-cache-dir -r requirements.txt
# RUN chmod +x app.py 

# EXPOSE 8501

# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
