import re
from itertools import permutations
def solution(expression):
    answer = []
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    for i in op :
        answer.append(calculate(expression, i))
    
    return max(answer)

def calculate(expression, op) :
    exp = re.split('([-|+|*])', expression)
    
    for i in op :
        stack = []
        while len(exp) != 0 :
            tmp = exp.pop(0)
            if tmp == i :
                stack.append(operation(stack.pop(), exp.pop(0), i))
            else :
                stack.append(tmp)
        exp = stack
    return abs(int(stack[0]))
            
        
def operation(num1, num2, op) :
    if op == "+" :
        return str(int(num1) + int(num2))
    if op == "-" :
        return str(int(num1) - int(num2))
    if op == "*" :
        return str(int(num1) * int(num2))