FROM python:latest
WORKDIR /src/
COPY main.py .
RUN pip3 install docker
CMD ["python3", "src/main.py"]