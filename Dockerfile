FROM python:3

RUN apt-get update -y

WORKDIR /app

RUN pip3 install -r req*

COPY . .

CMD ["python", "-m", "PyroUbot"]
