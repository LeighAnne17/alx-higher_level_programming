#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -sL -X GET "$1" -o /dev/null && curl -sL "$1"
