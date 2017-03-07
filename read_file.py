#!/usr/bin/env python
# coding=utf-8
import csv

with open("hostnames.csv", newline='') as f:
    reader = csv.DictReader(f, fieldnames=('ip','host'))
    for row in reader:
        print(row['ip'], row['host'])
