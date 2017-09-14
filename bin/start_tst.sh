#!/bin/bash
root=`dirname $0`/..
source $root/env/bin/activate
nohup python $root/src/manage.py runserver 7042 >> $root/logs/nohup.out &
