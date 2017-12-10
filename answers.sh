#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"
for day in day*; do
    cd "$DIR/$day/" && ./answer.sh
done
