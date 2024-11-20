# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and Gunicorn
RUN pip install Flask gunicorn

# Expose the port that the app runs on
EXPOSE 5001

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]  
