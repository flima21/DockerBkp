FROM python:latest
WORKDIR /app

COPY src/main.py /app/main.py
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]  