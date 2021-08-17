FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app

WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt