FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive


RUN apt update && apt install -y \
    python3 \
    python3-pip \
    curl \
    && apt clean

WORKDIR /app
COPY . .

RUN pip3 install flask pytest
EXPOSE 5000
CMD ["python3","app.py"]
