FROM python:latest
COPY src/main.py .
WORKDIR /
RUN pip3 install docker
CMD ["python3", "src/main.py"]