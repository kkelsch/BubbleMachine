var express = require('express');
var router = express.Router();
var PubNub = require('pubnub');
module.exports = router;

function buttonClick(){
  alert('test');
}

// SUPER SECRET SHIT
var pubKey = '<secret>';
var subKey = '<secret>';
var channelName = 'Bubble-Channel'; 

var pubnub = new PubNub({
  publishKey : pubKey,
  subscribeKey : subKey
});

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'HYPE TIME' });
});

router.post('/sendMessage', function(req, res){
  publishMessage();
  next();
});

function publishMessage() {
      console.log("Sending message");
      var publishConfig = {
          channel : channelName,
          message : {
              title: "Hype Message",
              description: "ENGAGE HYPE"
          }
      };
      pubnub.publish(publishConfig, function(status, response) {
          console.log(status, response);
      });

};