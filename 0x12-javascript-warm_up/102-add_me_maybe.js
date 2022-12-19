#!/usr/bin/node
// a function that increments and calls a function
exports.addMeMaybe = function (n, myFunction) {
  myFunction(n + 1);
};
