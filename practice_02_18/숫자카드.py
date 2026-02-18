import sys 
sys.stdin = open("input.txt", "r")
# cnt_list = [0] * 10
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    numbers = list(map(int, input()))
    cnt_list = [0] * 10
   
    for n in numbers:
        cnt_list[n] +=1

    max_cnt = 0
    max_idx = 0
    for i in range(10):
        if cnt_list[i] >= max_cnt:
            max_cnt = cnt_list[i]
            max_idx = i
    print(max_cnt, max_idx)        

        

       
            


        
        

        
       

        
        
# for i in range(10): #0~9까지
#     print(result.count(str(i)))

            