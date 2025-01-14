#!/usr/bin/env bash
set -e
cd $(pwd)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt