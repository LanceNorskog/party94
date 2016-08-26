# FROM registry.edmodo.io/base
FROM ubuntu:12.04

WORKDIR /root

RUN DEBIAN_FRONT_END=noninteractive apt-get update

RUN DEBIAN_FRONT_END=noninteractive apt-get update
RUN DEBIAN_FRONT_END=noninteractive apt-get install -y python-software-properties
RUN DEBIAN_FRONT_END=noninteractive apt-get install -y git
RUN DEBIAN_FRONT_END=noninteractive apt-get install -y postgresql-client 

RUN apt-get install -y python-pip python2.7-dev

RUN apt-get install -y libpq-dev

RUN pip install PyGreSQL
RUN pip install wheel

RUN pip install flask

RUN apt-get install -y curl
RUN apt-get install -y net-tools

RUN pip install shelljob
