#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], { encoding: 'utf8' }, (err, content) => {
  if (err) return console.error(err);

  console.log(content);
});
