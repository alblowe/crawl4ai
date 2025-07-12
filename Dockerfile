# Dockerfile

FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# System dependencies
RUN apt-get update && apt-get install -y \
    curl wget git build-essential \
    libglib2.0-0 libnss3 libatk1.0-0 libcups2 libx11-xcb1 libxcomposite1 \
    libxdamage1 libxrandr2 libxext6 libxfixes3 libxrender1 libxkbcommon0 \
    libasound2 libdrm2 libx11-6 libxcomposite1 libxdamage1 libxrandr2 \
    libgbm1 libpango-1.0-0 libcairo2 libatspi2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python deps
RUN pip install --upgrade pip && \
    pip install crawl4ai fastapi uvicorn

# Install Playwright + dependencies
RUN playwright install --with-deps

# Copy API file
COPY app.py /app.py

# Expose port
EXPOSE 8000

# Run it
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
