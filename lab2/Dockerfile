FROM python:3.10.0-alpine3.14
WORKDIR /app
COPY . .
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 8080
CMD ["python", "src/main.py"]

