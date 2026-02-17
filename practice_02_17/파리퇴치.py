# SWEA 2001번
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    # 좌표 진입
    for i in range(N):
        for j in range(N):
            current_sum =0 # 새로운 좌표를 갈 때마다 누적값 초기화
            # 파리채 면적(MxM만큼 탐색)
            for r in range(M): #range(N-M+1)을 했으면 범위확인 if문(x)
                for c in range(M):
                    # i + r, c만큼이 범위 밖을 나가는지 확인
                    if 0 <= i +r < N and 0 <= j+c < N:
                        current_sum += grid[i+r][j+c]
            if current_sum >= max_sum:
                max_sum = current_sum

    print(f"#{tc} {max_sum}")            
                    