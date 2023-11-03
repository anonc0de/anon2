FROM ohshin/ubot:dev

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -U -r req*

COPY . .

CMD ["python", "-m", "PyroUbot"]
 
