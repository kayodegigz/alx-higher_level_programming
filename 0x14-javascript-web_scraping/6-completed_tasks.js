#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const users = {};
    const todoResp = JSON.parse(body);

    for (let i = 0; i < todoResp.length; i++) {
      if (todoResp[i].completed === true) {
        if (todoResp[i].userId in users) {
          users[todoResp[i].userId]++;
        } else {
          users[todoResp[i].userId] = 1;
        }
      }
    }
    console.log(users);
  }
});
