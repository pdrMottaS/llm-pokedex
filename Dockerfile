FROM python:3.13.3-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]