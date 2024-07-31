#!/usr/bin/node

const request = require('request');
request.get({ url: process.argv[2], json: true }, (err, res, body) => {
  if (err) return console.error(err);
  const ntasks = {};
  for (const key in body) {
    const task = body[key];
    if (!Object.hasOwn(ntasks, task.userId)) {
      ntasks[task.userId] = 0;
    }
    if (task.completed) {
      ntasks[task.userId]++;
    }
  }
  console.log(ntasks);
});
