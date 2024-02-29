#!/bin/bash
# Takes in a URL - Displays
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
