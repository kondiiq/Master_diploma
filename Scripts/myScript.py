import numpy as np
import matplotlib as mlt


def create_val_weight_ratio_list(weight_lst, values_lst):
    sol = []
    length = len(values_lst)
    for element in range(0, length):
        sol.append(values_lst[element] / weight_lst[element])
    return sol


def divide_to_smaller_lists(ratio_list, numb_elements):
    return [ratio_list[element:element + numb_elements] for element in range(0, len(ratio_list), numb_elements)]


def choose_best_ratio(*smaller_port):  # means many argument not depend of number in arg list
    bst = []
    for my_port in smaller_port:
        for element in my_port:
            bst.append(max(element))
    return bst


def calculate_current_knapsack_status(best_ratio_list, val_lst, weight_lst, ratio_lst):
    removed_weight = []
    removed_val = []
    for element in best_ratio_list:
        index_ratio = ratio_lst.index(element)
        print(f"Finded index is:{index_ratio - 1}\n")
        removed_weight.append(weight_lst[index_ratio])
        removed_val.append(val_lst[index_ratio])
        del val_lst[index_ratio]
        del weight_lst[index_ratio]
        del ratio_lst[index_ratio]
    return removed_val, removed_weight, ratio_lst


if __name__ == "__main__":
    max_capacity = 750
    weight_list = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240, 150]
    values_list = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120, 729]
    solution_list = create_val_weight_ratio_list(weight_list, values_list)
    list_len = len(solution_list)
    smaller_portions = []
    if len(values_list) < 10:
        while len(values_list) % 2:
            solution_list.append(0 / 1)
        smaller_portions = divide_to_smaller_lists(solution_list, 2)
    if 10 <= len(values_list) <= 29:
        while len(solution_list) % 3 != 0:
            print('Not divide by 3')
            solution_list.append(0 / 1)
        if len(solution_list) % 3 == 0:
            smaller_portions = divide_to_smaller_lists(solution_list, 3)
    '''if len(values_list) >= 30 and len(values_list) <= 49:
        while len(solution_list) % 5 != 0:
            solution_list.append(0/1)
        if len(solution_list) % 5:
            smaller_portions = divide_to_smaller_lists(solution_list, 5)
    if len(values_list) >= 50 and len(values_list) <= 89:
        while len(solution_list) % 7 != 0:
            smaller_portions = solution_list.append(0/1)
        if len(solution_list) % 7:
            smaller_portions = divide_to_smaller_lists(solution_list, 7) '''
    best_current_ratio = choose_best_ratio(smaller_portions)
    removed_elements_value, removed_elements_weight, solution_list\
        = calculate_current_knapsack_status(best_current_ratio, values_list, weight_list, solution_list)
    print(f'Current knapsack Values is :{sum(removed_elements_value)}\n'
          f' Current knapsack Weight is : {sum(removed_elements_weight)}\n'
          f'Remain{max_capacity - sum(removed_elements_weight)} Weight units')
