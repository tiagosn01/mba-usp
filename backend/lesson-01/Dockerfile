# Use the Python 3.12 image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy all your Python files to the container
COPY . .

RUN pip install --no-cache-dir requests

# Define the command to run your application
# CMD ["python", "your_main_script.py"]
CMD ["tail", "-f", "/dev/null"]
