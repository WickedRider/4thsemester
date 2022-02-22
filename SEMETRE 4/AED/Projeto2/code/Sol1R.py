from datetime import datetime as dt
from sys import stdin, stdout, exit
import random as r

def readln():
    input = ["0", "1"]
    input[0] = stdin.readline()
    input[1] = stdin.readline().strip().split(' ')
    return input

def outln(n):
    stdout.write(str(n))
    stdout.write('\n')

def main():
    #input = readln()
    array = []
    SIZE = 150000
    array = fill(array, SIZE)
    time_begin = dt.now()
    array = sorted(array)
    valor_final = improved1(array, SIZE)
    print(valor_final)
    time_end = dt.now() - time_begin
    print("Execution Time: ")
    print(time_end)

def fill(arr, num):
    for i in range(num):
        arr.append(r.randint(0, 100000))
    
    return arr

def checkSize(size, arr):
    for i in arr:
        if(int(i) > 1000000 or int(i) < 0):
            exit(1)
    if(size != len(arr)):
        print("Invalid Size. Exit")
        exit(1)

def improved1(arr, size):
    return abs(int(arr[0]) - int(arr[size-1]))
    

main()