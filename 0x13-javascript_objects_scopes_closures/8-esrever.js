#!/usr/bin/node
exports.esrever = function (list) {
  let last = (list.length) - 1;
  let j = 0; // idx of new list
  for (let i = last; (i - j) > 0; i--) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j++;
  }
  return list;
};
