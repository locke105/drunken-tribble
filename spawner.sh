#!/bin/bash

for proc in {1..30}; do
    time python client.py $proc 8081 &
done

wait
