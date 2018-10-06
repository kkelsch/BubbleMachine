// var http = require('http');
// //var express = require('express');
// //const app = new express();
// var fs = require('fs');

// var server = http.createServer(function(request, response) {

//     response.writeHead(200, {"Content-Type": "text/plain"});
//     response.write(html);  
//     response.end();  

// });

// fs.readFile('./index.html', function (err, html) {



// var port = process.env.PORT || 1337;
// server.listen(port);

// console.log("Server running at http://localhost:%d", port);
var express = require('express');
var app = express();
var path = require('path');

app.use(express.static(__dirname + '/public'));

// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(8080);