FROM debian:bullseye-slim

RUN echo "America/Lima" > /etc/timezone
RUN date