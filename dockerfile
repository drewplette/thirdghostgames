# Dockerfile
FROM python:3.11-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .
RUN python manage.py collectstatic --noinput

# Run server
CMD ["gunicorn", "thirdghostgames.wsgi:application", "--bind", "0.0.0.0:8000"]
