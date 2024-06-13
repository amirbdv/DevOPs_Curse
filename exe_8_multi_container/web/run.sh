#!/bin/bash

docker_compose_dir="/home/mushra/exe_8_multi_container/web"

cd "$docker_compose_dir" || exit

docker-compose up --build -d
