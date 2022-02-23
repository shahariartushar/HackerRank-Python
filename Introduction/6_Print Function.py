#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from __future__ import print_function

def print_function(n):
    i = 1
    
    while i<=n:
        print (i, end='')
        i += 1
    

if __name__ == '__main__':
    n = int(raw_input())
    
    print_function(n)
