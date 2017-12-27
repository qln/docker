#!/bin/bash
nginx
uwsgi --ini /usr/local/app/uwsgi.ini
