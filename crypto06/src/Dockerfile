FROM python:3.11.6-alpine3.17

COPY ./src/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./src /app
WORKDIR /app

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5001", "app:app"]