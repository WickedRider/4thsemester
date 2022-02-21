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
    time_begin = dt.now()
    SIZE = int(input[0])
    array = input[1]
    checkSize(SIZE, array)
    final_value = exaustiveSearch(array)
    outln(str(final_value))
    
    time_end = dt.now() - time_begin
    #print("Execution Time: ")
    #print(time_end)



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