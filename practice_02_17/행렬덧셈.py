import sys
sys.stdin = open("input.txt", "r")

N , M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
result = [[0] * M for _ in range(N)]
# print(result)
for i in range(N):# 행 반복
    for j in range(M): # 열 반복
        result[i][j] = arr[i][j] + arr2[i][j]

for row in result:
    print(*row) 

# 다른 방법      
# 기존 result 생성 대신
# for i in range(N):
#     for j in range(M):
#         arr[i][j] += arr2[i][j]  # arr의 기존 값에 arr2 값을 누적

# # 출력은 똑같이 arr를 사용
# for row in arr:
#     print(*row)