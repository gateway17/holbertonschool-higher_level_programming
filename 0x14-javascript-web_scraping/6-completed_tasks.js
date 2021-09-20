#!/usr/bin/nodejs
const request = require('request');
const URL = process.argv[2];
request(URL, function (error, response, body) {
  if (error) throw error;
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
