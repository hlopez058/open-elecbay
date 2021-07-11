FROM python:3-alpine

# FLASK SERVER SETUUP
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

EXPOSE 5001
CMD ["flask", "run","-p","5001"]
