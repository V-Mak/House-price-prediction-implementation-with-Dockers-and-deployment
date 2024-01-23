FROM python:3.9.5-slim-buster
COPY . /app
WORKDIR /app
RUN apt update -y && apt install awscli -y
RUN pip install -r requirement.txt
CMD ["python3", "app.py"]