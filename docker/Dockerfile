FROM python:3.10-slim

WORKDIR /app

# Install system dependencies FIRST
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1 \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip (important for torch + faiss)
RUN pip install --upgrade pip

# Copy requirements separately (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000
EXPOSE 8501

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]