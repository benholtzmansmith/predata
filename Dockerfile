FROM ubuntu

MAINTAINER Ben Smith

RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing && \
  apt-get install -y \
   build-essential \
   gfortran \
   cython \
   python-all-dev \
   python-dev \
   python-pip \
   python-nose \
   python-h5py \
   git \
   wget && \
  pip install flask
  pip install requests

CMD src/server.py