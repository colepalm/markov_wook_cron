# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install cron
RUN apt-get update && apt-get install -y cron

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variable for Chrome to run in headless mode
ENV CHROME_BIN="/usr/bin/chromium-browser"

# Install Chromium and Chrome WebDriver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver

# Run the Python script as a cron job
CMD ["python", "src/test/test.py"]
