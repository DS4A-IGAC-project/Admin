#!/bin/bash

cd $HOME/Documents/DS4A/IGAC-admin

source .venv/bin/activate

cd IGAC

gunicorn IGAC.wsgi -w4 -b 0.0.0.0:8000
