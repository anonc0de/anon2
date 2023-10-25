FROM python:3

RUN apt-get update -y

WORKDIR /app

RUN pip3 install -U -r req*

COPY . .

CMD ["python", "-m", "PyroUbot"]
