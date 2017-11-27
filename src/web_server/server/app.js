var bodyParser = require('body-parser');
var cors = require('cors')
var express = require('express');
var path = require('path');

// routers
var index = require('./routes/index')
var requestPage = require('./routes/request')
var historyPage = require('./routes/history')
var app = express()

// view engine setup
app.set('views', path.join(__dirname, '../client/build/'));
app.set('view engine', 'jade');
app.use('/static', express.static(path.join(__dirname, '../client/build/static/')));


app.use(cors())
app.use(bodyParser.json())
app.use('/', index)
app.use('/requestForm', requestPage)
app.use('/history', historyPage)

app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  res.send('404 Not Found');
});

module.exports = app;
