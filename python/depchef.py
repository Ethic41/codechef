# Author : Dahir Muhammad Dahir
# Date: 18-02-2019

T = int(input())
for i in range(T):
    N = int(input())
    attacks = input().split(" ")
    defenses = input().split(" ")
    current_best_shield_value = -1
    for defence_index in range(len(defenses)):
        if defence_index == 0:
            defence = int(defenses[0])
            attack = int(attacks[1]) + int(attacks[-1])
            if (defence > attack) and (defence > current_best_shield_value):
                current_best_shield_value = defence
        elif defence_index == N - 1:
            defence = int(defenses[N - 1])
            attack = int(attacks[N - 2]) + int(attacks[0])
            if (defence > attack) and (defence > current_best_shield_value):
                current_best_shield_value = defence
        else:
            defence = int(defenses[defence_index])
            attack = int(attacks[defence_index - 1]) + int(attacks[defence_index + 1])
            if (defence > attack) and (defence > current_best_shield_value):
                current_best_shield_value = defence
    print(current_best_shield_value)