#!/usr/bin/env python3

a = 10

def add_one():
    global a
    a += 1

print(a)
add_one()
print(a)