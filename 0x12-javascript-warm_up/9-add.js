#!/usr/bin/node
function add(a, b)
{
  sum = a + b;
  console.log(sum);
}
a = parseInt(process.argv[2]);
b = parseInt(process.argv[3]);
add(a, b);
