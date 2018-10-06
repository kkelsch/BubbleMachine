var express = require('express');
var router = express.Router();
var PubNub = require('pubnub');
module.exports = router;

// SUPER SECRET SHIT
var pubKey = 'pub-c-1b8f92cc-6dbb-47f0-b329-bcf297c85cda';
var subKey = 'sub-c-b15b8210-bea3-11e8-8fd2-4a2bdf4876be';
var channelName = 'Bubble-Channel'; 

var pubnub = new PubNub({
  publishKey : pubKey,
  subscribeKey : subKey
});

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'ENGAGE HYPE' });
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