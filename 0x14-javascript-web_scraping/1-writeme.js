#!/usr/bin/nodejs

const fs = require('fs');

const STRING = process.argv[3];
const FILENAME = process.argv[2];

fs.writeFile(FILENAME, STRING, error => {
  if (error) { console.log(error); }
});
