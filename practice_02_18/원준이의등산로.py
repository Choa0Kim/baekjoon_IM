import sys
sys.stdin = open("input.txt", "r")

T = int(input())
#상하좌우 위치값 지정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, 1+T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0
    # 좌표 진입
    for i in range(N):
        for j in range(N):       
            # low_idx = grid[nr][nc]
            # 상하좌우 탐색
            r, c = i ,j
            cnt = 1  # 시작점도 1
            while True:
                next_r, next_c = -1, -1 # 초기화
                min_h = 101
                
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    # 범위 확인
                    if 0 <= nr < N and 0 <= nc < N:
                        # 상하좌우 중 작은 값 찾기
                        # 다음칸이 현재 칸 보다 작으면
                        if grid[nr][nc] < grid[r][c] and grid[nr][nc] < min_h:
                            # 최소값 갱신
                            min_h = grid[nr][nc]
                            next_r, next_c = nr, nc #최저 위치 저장
                # 상하좌우 확인 후 갈 곳 결정
                if next_r != -1 :
                    r, c = next_r, next_c
                    cnt +=1
                else:
                    break   

            if cnt > max_len:
                max_len = cnt      
    print(f'#{tc} {max_len}') 