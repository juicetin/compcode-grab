#!/bin/bash

folder=./imgs

inotifywait -m -q -e create -r $folder | while read file
do
    python utils/classify.py
    sleep 5
done
