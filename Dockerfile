# # Use the official Python image
# FROM --platform=linux/amd64 python:3.8-slim as base

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the application code
# COPY . .

# # Make port 8501 available to the world outside this container
# EXPOSE 8501

# # Set environment variables from .env file
# ENV $(cat .env | xargs)

# # Run the Streamlit app
# CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=$PORT"]


FROM python:3.7

# Expose port you want your app on
EXPOSE 8080

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy app code and set working directory
COPY app.py app.py

# Set environment variables from .env file
ENV $(cat .env | xargs)

# Run
ENTRYPOINT ["streamlit", "run", "app.py", "–server.port=8080", "–server.address=0.0.0.0”]
# CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=$PORT"]