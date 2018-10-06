var express =require('express');
var app = express();
var port=process.env.PORT || 3000;
var PubNub = require('pubnub');

// SUPER SECRET SHIT
var pubKey = 'pub-c-1b8f92cc-6dbb-47f0-b329-bcf297c85cda';
var subKey = 'sub-c-b15b8210-bea3-11e8-8fd2-4a2bdf4876be';
var channelName = 'Bubble-Channel'; 

var pubnub = new PubNub({
    publishKey : pubKey,
    subscribeKey : subKey
  });


app.use(express.static(__dirname + '/public'));

app.get('/',function(req,res){
console.log('hello from server');
 res.render('./public/index.html');
});

// call from front end
app.post('/sendMessage', function(req, res) {
    publishMessage(); 
});

// Publish Message
function publishMessage() {
    console.log("Sending message....");
    var currentTime = new Date();
    var publishConfig = {
        channel : channelName,
        message : {
            title: "Hype Message",
            description: "ENGAGE HYPE:" + currentTime.toLocaleTimeString()
        }
    };
    pubnub.publish(publishConfig, function(status, response) {
        console.log(status, response);
        
    });
};


app.listen(port);
console.log('Server Listening at port'+port);