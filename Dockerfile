FROM python:3.6-slim

#installing  requirements
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /app
VOLUME /app
WORKDIR /app

COPY app.py /app

EXPOSE 5000

CMD [ "python","-m","flask","run", "--host=0.0.0.0"]
