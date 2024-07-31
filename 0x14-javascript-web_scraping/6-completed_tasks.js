#!/usr/bin/node
// Script that computes the number of tasks completed by user

const request = require('request');

const apiUrl = process.argv[2]; // API URL from the command line argument

request.get(apiUrl, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }

    try {
        const tasks = JSON.parse(body);
        const userTasks = {};

        tasks.forEach(task => {
            if (task.completed) {
                if (userTasks[task.userId]) {
                    userTasks[task.userId]++;
                } else {
                    userTasks[task.userId] = 1;
                }
            }
        });

        console.log(userTasks);
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});
