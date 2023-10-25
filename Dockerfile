FROM python:3

WORKDIR /app

RUN apt-get update -y

RUN pip3 install -U pip

RUN pip3 install -U -r req*

COPY . .

CMD ["python", "-m", "PyroUbot"]
