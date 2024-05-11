FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

COPY . .

# Install Flask and other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the command to start the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]