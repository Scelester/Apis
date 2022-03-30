#!/bin/bash

cd Api_l
gunicorn Api_l.wsgi:application