#!/usr/bin/node

const list = require('./100-data.js').list;

const nl = list.map((el, i) => el * i);
console.log(list);
console.log(nl);
