FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python python-pip

ADD . /src
WORKDIR /src
RUN pip install -r house_listing_pipeline/requirements.txt
CMD ["python", "house_listing_pipeline/filter/house_listing_filter_loop.py"]
