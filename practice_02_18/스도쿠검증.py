import sys 
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    grid = [list(map(int, input().split())) for _ in range(9)]

    ans =1 # 전재조건 
    # 1. 가로, 세로 탐색
    # row_check = [0] * 10
    # col_check = [0] * 10
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10
        for j in range(9):
            # 가로 탐색
            row_num = grid[i][j] # 현재 위치의 값 확인
            # 만약 현재의 값이 체크박스안에 이미 있다면
            if row_check[row_num]:
                ans = 0 # 중복확인
                break # 루프 중단
            # 중복이 아니라면, 체크박스의 현 숫자를 1로 저장 =>방문기록 저장
            row_check[row_num] = 1
            #세로 탐색
            col_num = grid[j][i]
            if col_check[col_num]:
                ans = 0
                break
            col_check[col_num] = 1
        if ans == 0:
            break
    
    # 2. 3x3 박스 탐색 
    # check_box = [0] *10 
    # 좌표 진입
    for i in range(0, 9, 3): # 0~9까지 칸이 있고, 3칸씩 확인
        for j in range(0, 9, 3):
            # 박스 안 탐색
            check_box = [0] *10
            for r in range(3): # 3x3 이니까
                for c in range(3):
                    num = grid[i+r][j+c]
                    if check_box[num]:
                        ans = 0
                        break
                    check_box[num] = 1
    print(f'#{tc} {ans}')                
                        
                     
            
