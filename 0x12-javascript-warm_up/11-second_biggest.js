#!/usr/bin/node
const arr = process.argv.slice(2);
let int_arr = [];
if (arr.length < 2)
  console.log(1);
else
{
  for (i = 0; i < arr.length; i++)
    int_arr[i] = parseInt(arr[i]);
  const max_num = Math.max.apply(null, int_arr);
  int_arr.splice(int_arr.indexOf(max_num), 1);
  console.log(Math.max.apply(null, int_arr));
}
