# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables to avoid Python writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for Pillow and psycopg2
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev \
    && apt-get clean

# Copy requirements.txt to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the working directory
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000

# Run the Django development server (replace 'vmyasmart.wsgi:application' if needed)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "vmyasmart.wsgi:application"]
