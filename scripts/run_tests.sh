#!/bin/bash

BASEDIR=$(dirname $(readlink -f $(dirname $0)))

cd $BASEDIR
for d in embdgen-*; do
    if [ -d "$d/tests" ]; then
        echo "Testing $d"
        (
            cd $d
            umask 002 # Ensure a consistent umask
            pytest tests
        )
    fi
done
