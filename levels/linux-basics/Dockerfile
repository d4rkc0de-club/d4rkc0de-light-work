FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        bash \
        coreutils \
        findutils \
        procps \
        nano \
        vim-tiny \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Flags
COPY flag_easy.txt /flag_easy.txt
COPY flag_hard.txt /root/.flag_hard.txt

EXPOSE 5021

CMD ["python", "app.py"]