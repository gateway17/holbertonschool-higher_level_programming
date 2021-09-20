#!/usr/bin/nodejs

const request = require('request');

const ID = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/films/' + parseInt(ID);

console.log(api);

request(api, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
