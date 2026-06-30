# ── Stage 1: base image ──────────────────────────────────────────
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency list first (Docker layer cache optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose Flask port
EXPOSE 5000

# Health check — used by orchestrators to monitor container
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# Run the app
CMD ["python", "app.py"]
