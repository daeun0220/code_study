# 20115 에너지 드링크

n = int(input())
drink = list(map(int, input().split()))
drink.sort(key = lambda x : x , reverse = True)
ans = drink[0]
for i in range(1, n) :
    ans += drink[i]/2 
    
print(ans)
