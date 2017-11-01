FROM ubuntu:16.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y wget bzip2

RUN echo 'export PATH=/opt/miniconda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/miniconda && \
    rm ~/miniconda.sh

COPY ./requirements.yml /requirements.yml
RUN /opt/miniconda/bin/conda env create -f /requirements.yml

ENV PATH /opt/miniconda/envs/app/bin:$PATH
ENV C_FORCE_ROOT "true"

COPY . /

WORKDIR /app
