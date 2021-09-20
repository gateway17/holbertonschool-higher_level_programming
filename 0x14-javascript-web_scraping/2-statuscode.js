#!/usr/bin/nodejs

const request = require('request');

const TARGET = process.argv[2];
request.get(TARGET)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
