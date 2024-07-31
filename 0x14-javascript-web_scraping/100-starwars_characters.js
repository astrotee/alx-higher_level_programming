#!/usr/bin/node

const request = require('request');
const baseurl = 'https://swapi-api.alx-tools.com/api/films/';
request.get({ url: baseurl + process.argv[2], json: true }, (err, res, body) => {
  if (err) return console.error(err);
  for (const character of body.characters) {
    request.get({ url: character, json: true }, (err, res, body) => {
      if (err) return console.error(err);
      console.log(body.name);
    });
  }
});
