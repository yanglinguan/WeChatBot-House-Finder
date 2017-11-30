#FROM ubuntu:16.04
FROM node:9.2.0
#RUN apt-get update
#RUN apt-get install -y curl sudo
#RUN curl -sL https://deb.nodesource.com/setup_9.x |sudo -E bash -
#RUN apt-get install -y nodejs

ADD . /src
WORKDIR /src/client
RUN npm install
RUN npm run build

WORKDIR /src/server
RUN npm install

EXPOSE 3001
CMD npm start
