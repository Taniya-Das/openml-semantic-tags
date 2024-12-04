# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Update pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements and install dependencies
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose the API port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
