# 숫자 문자열과 영단어

a = "zero8six"
def sol(a):
    while a.isalpha():
        if "zero" in a:
            answer = a.replace("zero", '0')
            
        if 'six' in a:
            answer = a.replace('six', '6')
    return a
    

print(sol(a))