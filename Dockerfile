# Use the python:3.11 base image
FROM python:3.11

# Install necessary packages including Chromium
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    chromium

# Set ChromeDriver version (if needed)
ENV CHROME_DRIVER_VERSION="92.0.4515.107"

# Download and install ChromeDriver (if needed)
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /tmp \
    && mv /tmp/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver

# Set the working directory
WORKDIR /usr/src/tests

# Copy the project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the default command to run when the container starts
CMD ["python", "--version"]
