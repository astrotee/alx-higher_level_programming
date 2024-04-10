#!/usr/bin/node

const dict = require('./101-data.js').dict;

const nd = {};
for (const [key, val] of Object.entries(dict)) {
  if (val in nd === false) {
    nd[val] = [];
  }
  nd[val].push(key);
}
console.log(nd);
