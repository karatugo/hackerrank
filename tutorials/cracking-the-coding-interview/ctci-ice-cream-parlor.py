#!/bin/python

import sys

def solve(arr, money):
    cost_diffs = [money-c for c in arr]
    _ = arr[:]
    _.reverse()
    for c in cost_diffs:
        i = cost_diffs.index(c)
        j = _.index(c)
        l = len(arr)
        if c in arr and i != l-j:
            print str(i+1) + " " + str(l-j)
            return

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        money = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        solve(arr, money)

