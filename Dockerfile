FROM python:3.12-alpine3.20
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
VOLUME [ "/app/instance" ]
CMD ["python", "app.py"]