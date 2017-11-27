"use strict";

const express = require('express');
const rpc_client = require('../rpc_client/rpc_client');
const router = express.Router();
const validator = require('validator')

router.post('/userId/:userId', function(req, res, next) {
  console.log('Submit request...');
  const user_id = req.params['userId'];
  const validationReqsult = validateRequestForm(req.body);
  
  if (!validationReqsult.success) {
    console.log('validationResult failed');
    return res.status(400).json({
      success: false,
      message: validationResult.message,
      errors: validationResult.errors,
    });
  }

  req.body["user_id"] = user_id
  rpc_client.submitRequestForm(req.body, function(response) {
    res.json(response);
  });

});

router.delete('/userId/:userId/requestId/:requestId', function(req, res, next) {
  console.log('Delete request...');
  const user_id = req.params['userId'];
  const request_id = req.params['requestId'];

  rpc_client.deleteRequestForm(user_id, request_id, function(response) {
    res.json(response);
  });

});

function validateRequestForm(payload) {
  console.log(payload);
  const errors = {};
  let isFormValid = true;
  let message = '';

  if (!payload || !Array.isArray(payload.areas) || payload.areas.length === 0) {
    isFormValid = false;
    errors.areas = 'Please provide areas that you are looking for.';
  }

  if (!payload || typeof payload.city != 'string' || payload.city.trim().length == 0) {
    isFormValid = false;
    errors.city = "Please provide city that your are looking for.";
  }

  if (!isFormValid) {
    message = 'Check the form for errors.';
  }

  return {
    success: isFormValid,
    message,
    errors
  };
}

module.exports = router;
