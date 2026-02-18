import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    K = int(input())
    word = input()
    #빈 A인덱스 리스트
    a_idx = []
    # print(K, word)
    # 인덱스 리스트 
    for i in range(len(word)):
        if word[i] == 'A':
            a_idx.append(i)
    # print(a_idx)

    # K보다 존재하는 A의 갯수가 적은 경우
    if len(a_idx) < K:
        # 해당 케이스는 0을 출력하고 넘기기
        print(f'#{tc} 0')
        continue
    # a 인덱스 사이의 거리 측정
    max_len = 0
    # 현재 길이
    current_len= 0
    for i in range(len(a_idx)- K + 1):
        current_len = a_idx[i+K-1] - a_idx[i]
        if current_len >= max_len:
            max_len = current_len
    print(f'#{tc} {max_len}')        
        
            
            