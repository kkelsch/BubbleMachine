
var express = require('express');
var app = express();
var path = require('path');
var PubNub = require('pubnub');

// for style sheets
app.use(express.static(__dirname + '/public'));
app.use('/jquery', express.static(__dirname + '/node_modules/jquery/dist/'));

// SUPER SECRET SHIT
var pubKey = 'pub-c-1b8f92cc-6dbb-47f0-b329-bcf297c85cda';
var subKey = 'sub-c-b15b8210-bea3-11e8-8fd2-4a2bdf4876be';
var channelName = 'Bubble-Channel'; 

var pubnub = new PubNub({
    publishKey : pubKey,
    subscribeKey : subKey
  });



// endpoints
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});


app.get('/sendMessage', function(req, res) {
    publishMessage(); 
});

// Publish Message
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

console.log('Starting Site...');
app.listen(8080);
