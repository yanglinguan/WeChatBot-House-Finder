FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python python-pip

ADD . /src
ADD ../common/* /common
WORKDIR /src
RUN pip install -r requirements.txt
CMD ["./house_listing_pipeline_launcher.sh"]
