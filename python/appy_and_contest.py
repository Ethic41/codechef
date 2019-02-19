# Author : Dahir Muhammad Dahir
# Date: 18-02-2019

T = int(input())
for i in range(T):
    N, A, B, K = map(int, input().split(" "))
    problem_to_solve_counter = 0
    for j in range(1, N+1):
        if j % A == 0 and j % B == 0:
            pass
        elif j % A == 0:
            problem_to_solve_counter += 1
        elif j % B == 0:
            problem_to_solve_counter += 1
    if problem_to_solve_counter >= K:
        print("Win")
    else:
        print("Lose")