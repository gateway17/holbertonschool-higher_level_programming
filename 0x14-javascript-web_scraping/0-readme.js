#!/usr/bin/nodejs

const fs = require('fs');

const FILENAME = process.argv[2];
fs.readFile(FILENAME, (error, datos) => {
  if (error) { console.log(error); } else { console.log(datos.toString()); }
});
