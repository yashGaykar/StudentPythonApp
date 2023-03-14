FROM python:3.9-slim-buster

# RUN apk add --no-cache python3-dev \
#     && pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["./bootstrap.sh"]