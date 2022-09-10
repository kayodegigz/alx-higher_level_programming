#!/usr/bin/node
const arr = process.argv.slice(2);
const intArr = [];
if (arr.length < 2) { console.log(0); } else {
  for (let i = 0; i < arr.length; i++) { intArr[i] = parseInt(arr[i]); }
  const maxNum = Math.max.apply(null, intArr);
  intArr.splice(intArr.indexOf(maxNum), 1);
  console.log(Math.max.apply(null, intArr));
}
