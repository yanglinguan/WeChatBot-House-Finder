FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python python-pip

ADD . /src

WORKDIR /src
RUN pip install -r requirements.txt
CMD ["python", "service.py"]


