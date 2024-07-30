#!/usr/bin/node

const request = require('request');
const baseurl = 'https://swapi-api.alx-tools.com/api/people/';
request.get({ url: baseurl + 18, json: true }, (err, res, body) => {
  if (err) return console.error(err);
  console.log(body.films.length);
});
