#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // URL to request
const filePath = process.argv[3]; // File path to store the response

request.get(url, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }

    fs.writeFile(filePath, body, 'utf8', (writeErr) => {
        if (writeErr) {
            console.error(writeErr);
        }
    });
});
