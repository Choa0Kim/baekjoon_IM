# SWEA 2001번
import sys
sys.stdin = open("input2.txt", "r")
T = 2
# T = int(input())
# 상하좌우 지정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # print(grid)
    # 좌표 진입
    max_sum = 0
    for i in range(N):
        for j in range(N):
            # 위치 탐색
            current_sum = grid[i][j] # 한 좌표마다 초기화 되어야 함. + 현위치 값도 포함
            for k in range(4):
                for d in range(1, M):
                    nr = i + dr[k] * d
                    nc = j + dc[k] * d
                    # 범위 확인
                    # current_sum = 0 # 한 좌표마다 초기화 되어야 함.
                    if 0 <= nr < N and 0 <= nc < N:
                    # 1. 현 좌표의 상하좌우 값의 합 구하기
                        current_sum += grid[nr][nc]
              
            # 그중 가장 큰 값 갱신    
            if current_sum >= max_sum:
                max_sum = current_sum

    print(max_sum)


# T = 2
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             for k in range(M):
#                 nr = i + grid[i]
#                 nc = j + grid[j]



            
            



