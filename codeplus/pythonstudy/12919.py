# 12929 
s = list(input())
t = list(input())
answer = 0

def game(t) :
    global answer
    if len(t) == len(s):
        if t == s :
            answer = 1
        return
    
    if t[0] == "B" :
        t = t[::-1]
        t.pop()
        game(t)
        t.append("B")
        t = t[::-1]
    
    if t[-1] == "A" :
        t.pop()
        game(t)
        t.append("A")

game(t)
if answer == 1 :
    print(1)
else :
    print(0)

    



