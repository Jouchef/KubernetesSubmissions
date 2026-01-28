#!/usr/bin/env bash

rnd_url=$(curl -w "%{redirect_url}" -o /dev/null -s https://en.wikipedia.org/wiki/Special:Random)
task="Lue artikkeli aiheesta: ${rnd_url}"

echo "Lähetetään POST-pyyntö random urlista: ${rnd_ur}"
curl \
    -L -X POST http://backend-svc:2345/todostest \
    -d "task=$task"