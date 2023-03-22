# 20006 랭킹전 대기열

p, m = map(int,input().split())
user = []
for i in range(p) :
    l, n = input().split()
    user.append([int(l),n])

game, level = [], []
game.append([user[0]])
level.append(user[0][0])

for l, n in user :
    game_number = 0
    cnt = 1
    if len(game[game_number]) >= m :
        continue

    if level - 10 <= l <= level + 10 :
        game[game_number].append([l,n])
    
    elif l < level-10 or l > level+10 :
        game_number += 1
        game[game_number].append([l,n])