# 단어 공부
word = input()
word = word.upper()

word_list = list(set(word))
cnt_list = []
for i in word_list :
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  #cnt 최댓값 인덱스
    print(word_list[max_index])
