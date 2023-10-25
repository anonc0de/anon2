FROM python:3

RUN apt-get update -y

WORKDIR /app

COPY . .

RUN pip3 install -r req*

CMD ["python", "-m", "PyroUbot"]
