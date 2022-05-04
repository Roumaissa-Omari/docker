#syntax=docker/dockerfile:1
FROM python:3.8-slim-buster



COPY input.json /data/
COPY output.json /data/

RUN ls /data

