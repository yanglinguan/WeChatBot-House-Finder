FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python python-pip

ADD . /src
WORKDIR /src
RUN pip install -r house_listing_pipeline/requirements.txt
CMD ["./house_listing_pipeline/house_listing_pipeline_launcher.sh"]
