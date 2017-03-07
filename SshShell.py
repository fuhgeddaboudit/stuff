#!/usr/bin/env python
# coding=utf-8
import spur

shell = spur.SshShell(
    hostname="10.1.10.1",
    username="cisco",
    password="cisco"
)
with shell:
    result = shell.run(["echo","sh run"])
print(result.output)
