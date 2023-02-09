#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file
The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request */

const args = process.argv;
const requestURL = args[2];
const Path = args[3];
const fs = require('fs');
const req = require('request');

req(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(Path, body, 'utf8', function (error) {
      if (error) { console.log(error); }
    });
  }
});
