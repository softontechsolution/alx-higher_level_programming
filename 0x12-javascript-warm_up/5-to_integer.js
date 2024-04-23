#!/usr/bin/node

const arg = process.argv[2];

const convertedNumber = parseInt(arg);

console.log(isNaN(convertedNumber) ? 'Not a number' : 'My number: ' + convertedNumber);
