FROM python:3.9.5-slim-buster
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip && apt update -y && apt install awscli -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
CMD ["python3", "app.py"]
