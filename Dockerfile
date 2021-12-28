FROM python:3.10.1-slim

RUN apt-get update -y && apt-get update -y
RUN pip install --upgrade pip

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]