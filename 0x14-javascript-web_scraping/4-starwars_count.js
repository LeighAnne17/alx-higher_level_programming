#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2]; // API URL from the command line argument
const wedgeAntillesId = 18;    // Character ID for Wedge Antilles

request.get(apiUrl, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }

    try {
        const data = JSON.parse(body);
        let count = 0;
        
        data.results.forEach(movie => {
            if (movie.characters.some(characterUrl => characterUrl.endsWith(`/${wedgeAntillesId}/`))) {
                count++;
            }
        });
        
        console.log(count);
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});
