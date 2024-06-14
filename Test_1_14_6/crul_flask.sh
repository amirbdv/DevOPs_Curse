#!/bin/bash

num_of_words=$(curl http://localhost:8001/)

echo $num_of_words
