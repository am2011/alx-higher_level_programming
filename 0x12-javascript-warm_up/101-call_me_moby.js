#!/usr/bin/node
// executes x times a function
exports.callMeMoby = function (x, myFunction) {
  for (let i = 0; i < x; i++) {
    myFunction();
  }
};
