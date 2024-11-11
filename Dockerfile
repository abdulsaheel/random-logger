FROM python:3.10-slim

WORKDIR /app

COPY logger.py .

ENV LOG_FILE=/app/logs/app.log

RUN mkdir -p /app/logs

CMD ["python", "logger.py"]
