from datetime import datetime as dt
from sys import stdin, stdout, exit
import random as r


def main():
    SIZE = 10000
    array = []
    array = fill(array, SIZE)
    time_begin = dt.now()
    final_value = exaustiveSearch(array)
    time_end = dt.now() - time_begin
    print(time_end)

def fill(arr, num):
    for i in range(num):
        arr.append(r.randint(0, 100000))
    
    return arr

def checkSize(size, arr):
    if(size != len(arr)):
        print("Invalid Size. Exit")
        exit(1)

def exaustiveSearch(arr):
    now = 0
    for i in arr:
        for j in arr:
            value = abs(int(i) - int(j))
            if(value > now):
                now = value

    return now
    

main()