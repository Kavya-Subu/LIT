FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy everything from repo root into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run Django using Gunicorn
CMD ["gunicorn", "inventory.wsgi:application", "--bind", "0.0.0.0:8000"]

