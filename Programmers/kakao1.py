
def solution(survey, choices):
    n = len(choices)
    score = [[0,0] for _ in range(4)]
    ans = ''
    for i in range(n):
        if choices[i] == 5 or choices[i] == 6 or choices[i] == 7:
            if survey[i][1] == 'R':
                score[0][0] = choices[i] % 4
            elif survey[i][0] == 'T':
                score[0][1] = choices[i] % 4
            elif survey[i][1] == 'C':
                score[1][0] = choices[i] % 4
            elif survey[i][1] == 'F':
                score[1][1] = choices[i] % 4
            elif survey[i][1] == 'J':
                score[2][0] = choices[i] % 4
            elif survey[i][1] == 'M':
                score[2][1] = choices[i] % 4
            elif survey[i][1] == 'A':
                score[3][0] = choices[i] % 4
            elif survey[i][1] == 'N':
                score[3][1] = choices[i] % 4
        elif choices[i] == 1 or choices[i] ==2 or choices[i]==3:
            if survey[i][1] == 'R':
                score[0][0] = 4-choices[i]
            elif survey[i][0] == 'T':
                score[0][1] = 4-choices[i]
            elif survey[i][1] == 'C':
                score[1][0] = 4-choices[i]
            elif survey[i][1] == 'F':
                score[1][1] = 4-choices[i]
            elif survey[i][1] == 'J':
                score[2][0] = 4-choices[i]
            elif survey[i][1] == 'M':
                score[2][1] = 4-choices[i]
            elif survey[i][1] == 'A':
                score[3][0] = 4-choices[i]
            elif survey[i][1] == 'N':
                score[3][1] = 4-choices[i]

    if score[0][0] >= score[0][1]:
        ans = "R"
    else:
        ans = "T"
    if score[1][0] >= score[1][1]:
        ans = ans + 'C'
    else:
        ans += 'F'
    if score[2][0] >= score[2][1]:
        ans += 'J'
    else:
        ans += 'M'
    if score[3][0] >= score[3][1]:
        ans += 'A'
    else:
        ans += 'N'
    
    return ans 
            

survey = list(input().split())
choices = list(map(int,input().split()))
print(solution(survey, choices))