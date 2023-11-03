FROM ohshin/ubot:dev

WORKDIR /app

RUN pip3 install -U -r req*

COPY requirements.txt .

COPY . .

CMD ["python", "-m", "PyroUbot"]
 
