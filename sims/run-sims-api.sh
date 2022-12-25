#!/usr/bin/env bash
source venv/bin/activate
export FLASK_API=sims-api
export FLASK_ENV=development
flask run
deactivate
