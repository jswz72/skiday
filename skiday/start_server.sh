#!/usr/bin/env bash
if [ $1 == "dev" ]
then
    export FLASK_ENV=development
fi
export FLASK_APP=app.py
flask run