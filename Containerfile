FROM python:3.11-alpine

WORKDIR /code

COPY . .
COPY requirements.txt .

RUN apk update \
 && apk upgrade \
 && apk add bash git openssh vim libffi-dev gcc libc-dev linux-headers postgresql-dev ffmpeg 

RUN python3.11 -m pip install pip --upgrade
RUN python3.11 -m pip install git+https://github.com/openai/whisper.git

RUN pip install -r ./requirements.txt

# --proxi-headers is added when the container behind a TLS terminal proxy like nginx or traefik
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--reload"]
