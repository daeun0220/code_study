#1406 에디터    # 시간초과
def cursor(c, n_list ): # 뭔가 커서 인덱스도 줘야할거같은데...모르겠네
    if c == "L":
        cindex = n_list.index("cursor")
        if cindex == 0:
            return n_list        
        else:
            temp = n_list[cindex-1]
            n_list[cindex-1] = n_list[cindex]
            n_list[cindex] = temp
            return n_list
    if c == "D":
        cindex = n_list.index("cursor")
        if cindex == len(n_list)-1:
            return n_list
        else:
            temp = n_list[cindex]
            n_list[cindex] = n_list[cindex+1]
            n_list[cindex+1] = temp
    if c == "B":
        cindex = n_list.index("cursor")
        if cindex == 0:
            return n_list 
        else:
            del n_list[cindex-1]
            return n_list
    if "P" in c:
        cindex = n_list.index("cursor")
        c_str = c[2]
        n_list.insert(cindex, c_str)
        return n_list

n = input()
m = int(input())
n_list = [i for i in n]
editor = []
n_list.append("cursor")
for i in range(m):
    edit = input()
    editor.append(edit)
     # find 함수는 문자열의 위치 찾는 함수 index가 리스트

for i in range(m):
    cursor(editor[i],n_list)

n_list.remove("cursor")
print(''.join(n_list))


   

        






 

        


