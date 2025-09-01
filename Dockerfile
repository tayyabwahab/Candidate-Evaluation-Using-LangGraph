# Use Python 3.11 slim image as base
FROM python:3.11-slim


# Set working directory
WORKDIR /app


# Copy application code
COPY . .

# Install required dependencies
RUN pip install -r requirements.txt

# Default command to run the application
CMD ["python", "main.py"] 