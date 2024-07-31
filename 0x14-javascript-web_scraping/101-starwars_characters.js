#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:

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

        // Function to print character names in order
        function fetchCharacterName(index) {
            if (index >= characterUrls.length) return;

            request.get(characterUrls[index], (err, response, body) => {
                if (err) {
                    console.error(err);
                    return;
                }

                try {
                    const character = JSON.parse(body);
                    console.log(character.name);
                    // Fetch the next character
                    fetchCharacterName(index + 1);
                } catch (parseError) {
                    console.error('Error parsing JSON:', parseError);
                }
            });
        }

        // Start fetching characters
        fetchCharacterName(0);

    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});
