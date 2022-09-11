#!/usr/bin/node
const SquareN = require('./5-square');

class Square extends SquareN {
  charPrint (c) {
    if (!c) c = 'X';
    let row = '';
    for (let i = 0; i < this.width; i++) row += c;

    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
}

module.exports = Square;
