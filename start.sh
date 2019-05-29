#!/bin/bash

gunicorn -c gunicorn.cfg.py base.wsgi
