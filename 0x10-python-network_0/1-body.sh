#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -sL -X GET "$1" -o temp.txt && [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && cat temp.txt
