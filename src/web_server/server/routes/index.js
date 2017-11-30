var express = require('express');
var router = express.Router();
var path = require('path');

/* GET home page. */
router.get('/userId/:userId', function(req, res, next) {
  res.sendFile("index.html", { root:path.join(__dirname, '../../client/build/')});
});

module.exports = router;
