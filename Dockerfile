# Use the official Python image from the Python Docker Hub repository as the base image
FROM python:3.9-slim

# Set the working directory to /app in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Run main.py when the container launches
CMD ["python", "main.py"]