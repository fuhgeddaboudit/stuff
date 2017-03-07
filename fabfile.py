#!/usr/bin/env python2
# coding=utf-8
from fabric.api import run

def host_type():
    run('uname -a')

def host_date():
    run("date")
