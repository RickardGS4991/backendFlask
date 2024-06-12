FROM python:3.9-alpine

WORKDIR /technicaltest

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev python3-dev

COPY . /technicaltest

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]