#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let a = 0; a < x; a++) {
    theFunction();
  }
};
