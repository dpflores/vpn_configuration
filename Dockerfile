FROM debian:bullseye-slim

RUN sudo echo "America/Lima" > /etc/timezone
RUN date