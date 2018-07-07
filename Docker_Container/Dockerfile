FROM ubuntu:latest
# FROM debian:jessie-slim

RUN apt-get update

# Some of these packages may not necessary,
# Especially after line 13. 
#
RUN apt-get install -y \
python3 \
build-essential \
python3-pip \
python3-dev \
libsdl-image1.2-dev \
libsdl-mixer1.2-dev \
libsdl-ttf2.0-dev \
libsdl1.2-dev \
libsmpeg-dev \
python-numpy \
libportmidi-dev \
libfreetype6-dev \
libavformat-dev \
libswscale-dev 

RUN pip3 install pygame

# The Python GUI will NOT work if this directive was added in this Dockerfile and not in `docker run`,
#
# as this execution does not include the exports from the `docker run` command in "docker-build+run.sh"
#
# CMD python3 -m pygame.examples.aliens