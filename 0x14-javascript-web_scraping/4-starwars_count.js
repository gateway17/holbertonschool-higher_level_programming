#!/usr/bin/nodejs

const request = require('request');

let R_URL = process.argv[2];

R_URL = 'https://swapi-api.hbtn.io/api/people/18/';

request.get(R_URL, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).films.length);
});
