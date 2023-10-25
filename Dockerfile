FROM python:3

WORKDIR /app

RUN apt-get update -y

RUN pip3 install -U pip

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "PyroUbot"]
