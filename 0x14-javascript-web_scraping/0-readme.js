#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // First argument is the file path

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
