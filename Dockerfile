# ========================================
# Docker – Shri Ambika Sanskrit Mahavidyalaya
# ========================================
FROM python:3.12-slim

# OS Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install System deps (libpq required for PostgreSQL/Neon DB)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project code
COPY . .

# Build Tailwind CSS internally using the Python CLI tool
# (Downloads native CLI binary automatically without NodeJS)
RUN python manage.py tailwind build

# Collect all static files for WhiteNoise compression
# (Errors ignored via 'true' if no files exist initially)
RUN python manage.py collectstatic --noinput --settings=ambika.settings.production || true

# Prepare Persistent Data Directories (Crucial for Fly.io storage bindings)
RUN mkdir -p /app/media && chmod -R 777 /app/media
RUN mkdir -p /app/staticfiles && chmod -R 777 /app/staticfiles

# Expose HTTP port
EXPOSE 8000

# Launch Gunicorn Server
CMD ["gunicorn", "ambika.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
