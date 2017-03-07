#!/usr/bin/env python
# coding=utf-8
import base64
import paramiko

key = paramiko.RSAKey(data=base64.b64decode(b'AAA
