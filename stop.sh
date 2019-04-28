#!/bin/bash
pid_file='/tmp/gunicorn.pid'

[[ ! -f $pid_file ]] && echo "$pid_file not find" && exit 1
pid=$(cat $pid_file)
kill -TERM $pid
