# ========================================
# Docker – Shri Ambika Sanskrit Mahavidyalaya
# ========================================
FROM python:3.12-slim

# Env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ambika.settings.production

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Node deps (Tailwind)
COPY package.json tailwind.config.js ./
RUN npm install

# Copy project
COPY . .

# Build Tailwind
RUN npm run build

# Collect static
RUN python manage.py collectstatic --noinput --settings=ambika.settings.production || true

# Expose
EXPOSE 8000

# Run
CMD ["gunicorn", "ambika.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
