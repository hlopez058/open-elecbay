FROM python:3-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache mosquitto
RUN apk add --no-cache mosquitto-clients
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./app /usr/src/app
RUN /usr/sbin/mosquitto
EXPOSE 5000
CMD ["flask", "run"]

#ENTRYPOINT ["python3"]
#CMD ["-m","app.py"]