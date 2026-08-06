FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV OLLAMA_HOST=http://ollama-service:11434

CMD ["python", "app.py"]
