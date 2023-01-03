FROM debian:bullseye-slim

RUN echo "America/Lima" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN date