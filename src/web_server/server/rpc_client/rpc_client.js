const jayson = require('jayson');


// Create a client connected to backend server
var client = jayson.client.http({
  port: 4040,
  hostname: 'localhost'
});

function submitRequestForm(request_form, callback) {
  console.log(request_form)
  client.request('submitRequestForm', [request_form], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
}

function getRequestHistory(user_id, callback) {
  client.request('getRequestHistory', [user_id], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
      
}

function getRequestDetail(user_id, request_id, callback) {
  client.request('getRequestDetail', [user_id, request_id], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
      
}

function deleteRequestForm(user_id, request_id, callback) {
  client.request('deleteRequestForm', [user_id, request_id], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
}

module.exports = {
  submitRequestForm: submitRequestForm,
  getRequestHistory: getRequestHistory,
  deleteRequestForm: deleteRequestForm,
  getRequestDetail: getRequestDetail,
};
