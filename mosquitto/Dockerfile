FROM python:3-alpine
# MQTT BROKER SETUP
COPY ./config/mosquitto.conf /etc/mosquitto/mosquitto.conf
RUN apk add --no-cache mosquitto
RUN apk add --no-cache mosquitto-clients
RUN apk add curl
EXPOSE 1883
CMD ["/usr/sbin/mosquitto","-c","/etc/mosquitto/mosquitto.conf"]
