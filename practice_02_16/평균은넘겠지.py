import sys
sys.stdin = open("input.txt", "r")

C = int(input())

scores = [list(map(int, input().split())) for _ in range(C)]

# N = scores[1:]
# print(N)
for score in scores:
    mean = sum(score[1:]) / len(score[1:])
    cnt = 0
    for s in score[1:]:
        if s > mean :
            cnt += 1
    result = (cnt / len(score[1:])) * 100

    print(f'{result:.3f}%')