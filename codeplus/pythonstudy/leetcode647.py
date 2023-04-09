# 647

s = input()
cnt = 0
answer = []
for i in range(len(s)) :
    sub = s[i]
    sub_cnt = 0
    while len(sub) <= len(s) - i and sub_cnt <= len(s) - (i+1):
        if sub == sub[::-1] :
            cnt += 1
            answer.append(sub)
        sub_cnt += 1
        if sub_cnt > len(s) - (i+1) :
            continue
        else :
            sub += s[i+sub_cnt]

        

print(answer)