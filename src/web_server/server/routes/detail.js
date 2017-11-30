const express = require('express')
const rpc_client = require('../rpc_client/rpc_client');
const router = express.Router();

router.get('/userId/:userId/requestId/:requestId', function(req, res, next) {
  console.log('Get Request Detail...');
  user_id = req.params['userId'];
  request_id = req.params['requestId'];

  rpc_client.getRequestDetail(user_id,request_id, function(response) {
    res.json(response);
  });
});

module.exports = router;
