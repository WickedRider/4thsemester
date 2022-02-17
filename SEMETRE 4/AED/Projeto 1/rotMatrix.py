from sys import stdin, stdout 

class Mat:
    def __init__(self, matrix, angle):
        self.matrix = matrix
        self.angle = angle

    def rot(self, matrix, angle):



"""
    1 2 3                   8 5 1
    5 6 7           ->      9 6 2
    8 9 10                 10 7 3
    
    1 2                     5 3 1
    3 4             ->      2 4 6
    5 6               

    1 2 3                   4 1
    4 5 6           ->      5 2
                            6 3

"""


def readln():
    return stdin.readlines().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write('\n')

def mountMat():
    input = readln()
    n1,n2 = input[0], input[1]
    matrix = []
    for i in range(n1):
        temp = []
        for g in range(n2):
            temp.append(input[g])
        matrix.append(temp)
    

def main():
    