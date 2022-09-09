from python:3.7-alpine
WORKDIR /web
COPY main.py main.py
CMD [ "python3", "main.py"]
