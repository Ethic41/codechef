# Author : Dahir Muhammad Dahir
# Date: 19-02-2019

T = int(input())
for i in range(T):
    N, B = map(int, input().split(" "))
    current_max_area = 0
    for j in range(N):
        W, H, P = map(int, input().split(" "))
        if P <= B:
            area = W * H
            if area > current_max_area:
                current_max_area = area
    if current_max_area:
        print(current_max_area)
    else:
        print("no tablet")