from datetime import datetime as dt
from sys import stdin, stdout, exit

def readln():
    input = ["0", "1"]
    input[0] = stdin.readline()
    input[1] = stdin.readline().strip().split(' ')
    return input

def outln(n):
    stdout.write(str(n))
    stdout.write('\n')

def main():
    input = readln()
    #time_begin = dt.now()
    SIZE = int(input[0])
    array = sorted(input[1])
    checkSize(SIZE, array)
    min = int(array[0])
    max = int(array[SIZE-1])
    final_value = abs(min - max)
    outln(final_value)
    #time_end = dt.now() - time_begin
    #print("Execution Time: ")
    #print(time_end)



def checkSize(size, arr):
    for i in arr:
        if(int(i) > 1000000 or int(i) < 0):
            exit(1)
    if(size != len(arr)):
        print("Invalid Size. Exit")
        exit(1)

# def improved1(arr, size):
#     arr = sorted(arr)
#     return abs(int(arr[0]) - int(arr[size-1]))
    

main()