"""
[ref.href] www.hackerrank.com/challenges/python-lists
"""

from __future__ import print_function

cmds = {
    "insert"  : list.insert,
    "remove"  : list.remove,
    "append"  : list.append,
    "sort"    : list.sort,
    "pop"     : list.pop,
    "reverse" : list.reverse,
    "print"   : lambda L : print(L)
}

try:
    count = int(raw_input())
    L = []
    i = 0
    while i < count:
        cmdargs = raw_input().split()
        cmd = cmdargs[0]
        args = [int(arg) for arg in cmdargs[1:]]
        cmds[cmd](L, *args)
        i += 1
except (KeyError, ValueError) as e:
    raise e
