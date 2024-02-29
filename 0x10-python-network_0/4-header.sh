#!/bin/bash
# Takes in a URL - sends a GET request to the URL
curl -sX GET -H "X-School-User-Id: 98" "$1"
