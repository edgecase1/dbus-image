
FROM debian:bookworm-slim

RUN apt-get update -y && apt-get install -y python3-gi libgirepository1.0-dev dbus python3-dbus
RUN apt-get install -y can-utils
ADD service.py /app/service.py
COPY dbus-system.conf /etc/dbus-1/system.conf
RUN apt-get install -y procps iproute2 libcap2 iputils-ping curl
COPY start.sh /usr/local/bin
RUN chmod +x /usr/local/bin/start.sh
#CMD python3 /app/service.py


ENTRYPOINT ["/bin/bash", "/usr/local/bin/start.sh"]
