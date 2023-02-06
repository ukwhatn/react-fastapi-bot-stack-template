#!/bin/bash
cd "$(dirname "$0")"

# frontend init
docker-compose build
docker compose run --rm frontend sh -c "create-react-app app --template typescript"

# python requirements
pip install -r backend/requirements.txt
pip install -r db/requirements.txt
pip install -r bot/requirements.txt
