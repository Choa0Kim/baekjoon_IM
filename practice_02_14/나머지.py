import sys
sys.stdin = open("input.txt", "r")

# 항상 10개씩 들어옴
numbers = [int(input()) for _ in range(10)]
# print(N)

arr = []
for num in numbers :
    result = num % 42
    arr.append(result)

arr_set= set(arr)

print(len(arr_set))    


