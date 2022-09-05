#!/usr/bin/node
const argLen = process.argv.length;
console.log(argLen === 2 ? 'No argument' : argLen === 3 ? 'Argument found' : 'Arguments found');
