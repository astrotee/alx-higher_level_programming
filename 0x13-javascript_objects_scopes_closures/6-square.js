#!/usr/bin/node
const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    c ?? (c = 'X');
    for (let r = 0; r < this.height; r++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
