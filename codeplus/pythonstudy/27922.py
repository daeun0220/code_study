# 27922 현대모비스 입사 프로젝트

n, k = map(int, input().split())
sum1, sum2, sum3 = [], [], []
for i in range(n) :
    a, b, c = map(int, input().split())
    sum1.append(a+b)
    sum2.append(a+c)
    sum3.append(b+c)

sum1.sort(reverse = True)
sum2.sort(reverse = True)
sum3.sort(reverse = True)

ans1, ans2, ans3 = sum(sum1[:k]), sum(sum2[:k]), sum(sum3[:k])
print(max(ans1, ans2, ans3))




