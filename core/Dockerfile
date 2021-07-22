FROM python:3-alpine

# FLASK SERVER SETUUP
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

EXPOSE 1883
CMD ["python3","app.py"]
