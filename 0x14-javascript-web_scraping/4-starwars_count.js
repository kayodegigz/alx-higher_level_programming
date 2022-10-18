#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const response_body = JSON.parse(body);
    const res = response_body.results;
    let count = 0;
    for (let i = 0; i < res.length; i++) {
      const chars = res[i].characters;
      for (let j = 0; j < chars.length; j++) {
        const check_id18 = chars[j].endsWith('18/');
	if (check_id18) {
          count++;
	}
      }
    }
  console.log(count);
  }
});
