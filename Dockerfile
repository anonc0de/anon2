FROM ohshin/ubot:dev

WORKDIR /app

RUN pip3 install -U -r req*

COPY requirements.txt .

RUN pip3 install -U pip

COPY . .

CMD ["python", "-m", "PyroUbot"]
 
