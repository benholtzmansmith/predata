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
   python-requests \
   python-numpy \
   git \
   wget

RUN pip install --upgrade pip && \
   pip install flask==0.11.1

ADD src/ src/

ENV FLASK_APP="src/predata/server.py"

EXPOSE 5000

CMD flask run