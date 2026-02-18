# SWEA 1208번
import sys
sys.stdin = open("input3.txt", "r")
T = 10
for tc in range(1, 1+T):
    N = int(input())
    li = list(map(int, input().split())) 
    li_sort =sorted(li)  # li[0]이 가장 낮은 곳, li[99]가 가장 높은 곳
    # 덤프 수 만큼 for문 돌면서 평탄화 작업
    for i in range(N):
        # li_sort =sorted(li)
        li_sort[99] -= 1
        li_sort[0] += 1
        li_sort = sorted(li_sort)
    # N번 만큼 평탄화 하고 최종 최대-최소 값 구하기
    result = li_sort[99] - li_sort[0]   

    print(f'#{tc} {result}')


    
