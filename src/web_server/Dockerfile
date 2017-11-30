FROM node:9.2.0

ADD . /src
WORKDIR /src/client
RUN npm install
RUN npm run build

WORKDIR /src/server
RUN npm install

EXPOSE 3001
CMD npm start
