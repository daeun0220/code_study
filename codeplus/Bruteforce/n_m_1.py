# 15649  N과M(1)
'''
백트래킹
재귀함수나 DFS(깊이 우선 탐색)을 기반으로 불필요한 경우를 배제하며 원하는 해답에 도달할때까지 탐색하는 전략
스택(stack)을 이용해 퇴각
브루트포스 전략이나 처리 속도를 향상시키기 위해 가지치기가 중요한 역할을 한다
이 문제의 경우 
해당 경우의 수를 스택에 추가(push)하고 동작이 끝난후 
스택에서 빼는 작업이(pop) 필요하다
'''

N,M = map(int,input().split())

s = []
def backtracking():
    if len(s) == M:  # 탈출조건
        print(' '.join(map(str,s)))
        return    # 탈출 
    for i in range(1,N+1):
        if i in s:  # 이미 선택한 숫자 또 선택 안하게 가지치기
            pass
        s.append(i)  # 함수 호출 스택 사용하면 backtracking(s + [i]) 이런식이다
        backtracking()  # 다시 호출하는 이유는 if절 실행하라고
        s.pop()

backtracking()
