# 델타 검색
# 상하좌우 델타 값
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# # 5x5 배열에서 (2, 2) 위치의 상하좌우 값을 출력하라
# N = 5
# # 5 x 5 행렬
# arr = [[0] * N for _ in range(5)]
# # print(arr)
# r, c = 2, 2
# for i in range(4):
#     nr = r +dr[i]
#     nc = c +dc[i]

#     # 행렬 밖으로 나가는지도 확인
#     if 0 <= nr < N and 0 <= nc < N:
#         print(f"방향 {i}의 값:", arr[nr][nc])

# #-------------------------------
# # (2, 2) 위치의 상하좌우 합이 8이 나오는지 확인
# #상하좌우 위치값 설정
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# grid = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 2, 1, 1],
#     [1, 3, 0, 4, 1], # (2,2)는 0이고, 주변은 2, 3, 4, 5라고 가정
#     [1, 1, 5, 1, 1],
#     [1, 1, 1, 1, 1]
# ]
# #현재 위치 지정
# r, c = 2, 2

# #탐색
# total = 0
# for i in range(4):
#     #다음에 이동할 위치 지정
#     nr = r + dr[i]
#     nc = c + dc[i]
    
#     if 0 <= nr < 5 and 0 <= nc < 5 :
#         total += grid[nr][nc]
# print(total)

#------- 전체 탐색 연습 ----------
# 문제: N x N 지도의 모든 칸을 돌면서, 
# 각 칸의 상하좌우 인접한 값들의 합을 구하세요. 
# 그중 가장 큰 합은 얼마인가요?
# grid = [ # 연습용 격자 (IM 실전 느낌)
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [1, 3, 5, 2, 4],
#     [2, 4, 1, 3, 5],
#     [3, 1, 4, 5, 2]
# ]

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# # total= 0
# max_total = 0

# N = 5
# for i in range(N): #행 탐색
#     for j in range(N): # 열 탐색
#         total = 0
#         # 방향 탐색
#         for k in range(4):
#             nr = i + dr[k]
#             nc = j + dc[k]
    
#             if 0 <= nc < 5 and 0<= nr < 5:
#                 total += grid[nr][nc]
#         if total >= max_total:
#             max_total = total

# print (max_total) 

# # i, j: 좌표(행, 열)
# # K: 방향


# --------- 봉우리 찾기 문제-------
grid = [ # 연습용 격자 (IM 실전 느낌)
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 3, 5, 2, 4],
    [2, 4, 1, 3, 5],
    [3, 1, 4, 5, 2]
]

# 상하좌우 값 설정
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
N = 5
# 좌표 탐색
# is_peak = True  # 각 칸 마다 선언
cnt = 0
for i in range(N):
    for j in range(N):
        is_peak = True
        
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            # 유효한 범위의 값들만 비교
            if 0 <= nc < N and 0 <= nr < N:
                if grid[nr][nc] >= grid[i][j]:
                    is_peak = False
                    break
        if is_peak == True:
            cnt += 1
print(cnt)                    
                




