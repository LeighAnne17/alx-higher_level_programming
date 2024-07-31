#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2]; // Movie ID from the command line argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }

    try {
        const data = JSON.parse(body);
        const characterUrls = data.characters;

        characterUrls.forEach(url => {
            request.get(url, (err, response, body) => {
                if (err) {
                    console.error(err);
                    return;
                }

                try {
                    const character = JSON.parse(body);
                    console.log(character.name);
                } catch (parseError) {
                    console.error('Error parsing JSON:', parseError);
                }
            });
        });
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});
