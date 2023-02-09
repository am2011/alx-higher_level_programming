#!/usr/bin/node
/*a script that prints all characters of a Star Wars movie:
The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module request*/
const request = require('request');
const args = process.argv;
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(requestURL, function (error, response, body) {
if (error) {
    console.log(error);
  } else {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (error, response, body) {
      console.log(JSON.parse(body).name);
    });
   }
  }
});
