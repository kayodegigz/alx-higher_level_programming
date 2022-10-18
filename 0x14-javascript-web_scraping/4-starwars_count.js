#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const responseBody = JSON.parse(body);
    const res = responseBody.results;
    let count = 0;
    for (let i = 0; i < res.length; i++) {
      const chars = res[i].characters;
      for (let j = 0; j < chars.length; j++) {
        const checkId18 = chars[j].endsWith('18/');
        if (checkId18) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
