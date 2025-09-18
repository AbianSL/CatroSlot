#!/bin/bash

if [ ! -d ".venv" ]; then
    uv sync --no-dev
    echo -e "\nVirtual environment created and dependencies installed."
    sleep 2 
else
    source .venv/bin/activate
fi

python3 src/main.py
