#!/usr/bin/node

const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(link, function (_error, _response, body) {
  console.log(JSON.parse(body).title);
});
