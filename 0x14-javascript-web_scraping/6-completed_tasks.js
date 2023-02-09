#!/usr/bin/node
/* script that computes the number of tasks completed by user id
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
You must use the module request */

const args = process.argv;
const requestURL = args[2];
const req = require('request');
req(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const listTasks = JSON.parse(body);
    const result = {};
    for (let i = 0; i < listTasks.length; i++) {
      if (listTasks[i].completed === true) {
        if (result[listTasks[i].userId] === undefined) {
          result[listTasks[i].userId] = 0;
        }
        result[listTasks[i].userId] += 1;
      }
    }
    console.log(result);
  }
});
