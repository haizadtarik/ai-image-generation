# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY server.py app.py run.sh ./

RUN chmod +x run.sh

EXPOSE 8080 8501

ENTRYPOINT ["./run.sh"]