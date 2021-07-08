FROM docker.elastic.co/beats/filebeat:7.13.2
COPY ./config/filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
RUN mkdir /usr/share/filebeat/dockerlogs
USER filebeat