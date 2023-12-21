#!/bin/bash

BASEDIR=$(dirname $(readlink -f $(dirname $0)))

cd $BASEDIR
for d in embdgen-*; do
    echo "Linting $d"
    (
        cd $d
        hatch run pylint src
    )
done
