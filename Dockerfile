# Gebruik officiële Python image
FROM python:3.12-slim

# Zet werkdirectory
WORKDIR /app

# Kopieer requirements
COPY app/requirements.txt .

# Installeer dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer app code
COPY app .

# Expose poort
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
