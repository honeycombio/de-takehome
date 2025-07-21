FROM python:3.10-slim

# Install system dependencies including PostgreSQL client
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy pre-compiled bytecode and startup script
COPY __pycache__ ./__pycache__
COPY start.sh ./start.sh
COPY run_app.py ./run_app.py
RUN chmod +x ./start.sh

# Expose port
EXPOSE 5000

# Run the startup script
CMD ["bash", "./start.sh"]
