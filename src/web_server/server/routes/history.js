const express = require('express')
const rpc_client = require('../rpc_client/rpc_client');
const router = express.Router();

router.get('/userId/:userId', function(req, res, next) {
  console.log('Get Request History...');
  user_id = req.params['userId'];

  rpc_client.getRequestHistory(user_id, function(response) {
    res.json(response);
  });
});

module.exports = router;
