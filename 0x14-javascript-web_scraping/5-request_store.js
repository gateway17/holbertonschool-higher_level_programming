#!/usr/bin/nodejs

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const PATH = process.argv[3];

request.get(URL, function (error) {
  if (error) throw error;
}).pipe(fs.createWriteStream(PATH));
