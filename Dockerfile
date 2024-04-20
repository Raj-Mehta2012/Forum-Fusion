# # Use the official lightweight Python image.
# FROM python:3-slim

# # Set the working directory in the container.
# WORKDIR /app

# ENV HOST 0.0.0.0

# # Copy the application code and the .env file into the container.
# COPY . /app
# COPY .env /app/.env

# # Install dependencies.
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose port 8080 to the outside world.
# EXPOSE 8080

# # Make the entrypoint script executable.
# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh

# # Set the entrypoint to use the entrypoint script.
# ENTRYPOINT ["/app/entrypoint.sh"]


FROM python:3.8-slim

WORKDIR /app

ENV HOST 0.0.0.0

COPY . /app
COPY .env /app/.env

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x app.py 

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
