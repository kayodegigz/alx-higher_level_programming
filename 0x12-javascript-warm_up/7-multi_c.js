#!/usr/bin/node
const count = Math.floor(Number(process.argv[2]));
if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < count) {
    console.log('C is fun');
    i++;
  }
}
