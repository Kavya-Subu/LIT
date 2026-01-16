# Use Python 3.11 slim image
FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Force stdout/stderr to flush immediately
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app/inventory

# Copy all project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Start Django using Gunicorn
# wsgi.py is now in the same folder as manage.py (inventory/)
CMD ["gunicorn", "wsgi:application", "--chdir", "inventory", "--bind", "0.0.0.0:8000"]

