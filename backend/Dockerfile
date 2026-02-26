FROM python:3.11-slim

RUN addgroud -S fastapigroup && adduser -S fastapiuser -G fastapigroup

WORKDIR /app

RUN app-get update && app-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN  pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN mrdir -p static/images

RUN chmod -R 755 static

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
