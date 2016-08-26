# FROM registry.edmodo.io/base
FROM registry.edmodo.io/party94-base

WORKDIR /

COPY omg/pgpass root/.pgpass
RUN chmod 0600 root/.pgpass

WORKDIR /opt/edmodo/party94

COPY red.sh bin/red.sh

RUN git clone https://github.com/lance-edmodo/amazon-redshift-utils.git
# RUN git clone https://github.com/SimpleFinance/shiftmanager.git

RUN pip install -r amazon-redshift-utils/src/requirements.txt

COPY files/* .

CMD python party94.py
