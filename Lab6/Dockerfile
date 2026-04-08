FROM python:3.11-slim

WORKDIR /app

# Copy only the necessary files
# This ensures that unnecessary local files (README, .gitignore, etc) are not included
COPY requirements.txt .
COPY app.py .

# Install dependencies without cache for a smaller image
RUN pip install --no-cache-dir -r requirements.txt

# Cloud Run configuration
EXPOSE 8080
ENV PORT 8080

# Run the app
CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0
