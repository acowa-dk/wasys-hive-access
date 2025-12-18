FROM python:3.11-slim

# Set working directory to Django project root
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project files
COPY . .
COPY entrypoint.sh /app/entrypoint.sh

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Expose port
EXPOSE 8000

# Default command
ENTRYPOINT ["/app/entrypoint.sh"]