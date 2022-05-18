# 2609 최대공약수와 최소공배수

def maxans(a,b):
    a_list = []
    b_list = []
    ans = 1
    for i in range(1,a+1):
        if a % i == 0:
            a_list.append(i)
    for j in range(1,b+1):
        if b % j == 0:
            b_list.append(j)
    for k in range(len(a_list)):
        
        if a_list[k] in b_list:
            ans = max(ans, a_list[k])
        # else: ans = 1 을 넣을 경우 ans가 계속 1이 나올 수 있음 
    return ans

def minans(a,b):

    print(a*b//maxans(a,b))




a,b = map(int,input().split())
print(maxans(a,b))
minans(a,b)