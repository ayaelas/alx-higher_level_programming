#!/bin/bash
# Takes in a URL - sends a POST to the URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
