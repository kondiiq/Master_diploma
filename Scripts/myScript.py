import sys


def create_value_weight_ratio(values_lst, weight_lst):
    ratio_lst = []
    for element in range(0, len(values_lst)):
        ratio_lst.append(values_lst[element] / weight_lst[element])
    return ratio_lst


def divide_to_smaller_set(value_weight_lst, elements_in_set):
    return [value_weight_lst[element:element + elements_in_set] for element in
            range(0, len(value_weight_lst), elements_in_set)]


def choose_best_ratio(*smaller_portion):
    best_candidates = []
    for arrays in smaller_portion:
        for item in arrays:
            best_candidates.append((max(item)))
    return best_candidates


def find_element_in_main_set(item, main_set):
    return main_set.index(item)


def remove_element_from_main_set(main_set, candidate_index, values_lst, weight_lst):
    main_set.pop(candidate_index)
    weight_lst.pop(candidate_index)
    values_lst.pop(candidate_index)


def canIAddNewItem(current_capacity, weight_lst, main_set, knapsack_item, MAX_KNAPSACK_CAPACITY):
    if current_capacity + weight_lst[find_element_in_main_set(knapsack_item, main_set)] >= MAX_KNAPSACK_CAPACITY:
        return False


if __name__ == "__main__":
    MAX_CAPACITY = 250
    current_knapsack_status = 0
    current_knapsack_value = 0
    removed_values = []
    removed_weight = []
    indx_to_remove = []
    weight_list = [7, 1, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 36]
    values_list = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600]
    while current_knapsack_status + min(weight_list) < MAX_CAPACITY:
        val_wei_lst = create_value_weight_ratio(values_list, weight_list)
        smaller_sets = divide_to_smaller_set(val_wei_lst, 3)
        candidates = choose_best_ratio(smaller_sets)
        print(f"Val lst: {values_list} \n Weight lst: {weight_list}\n Ratio lst: {val_wei_lst}")
        print(f"Smaller sets {smaller_sets}")
        print(f"Candidates: {candidates}")
        for element in candidates:
            indx = find_element_in_main_set(element, val_wei_lst)
            current_knapsack_status += weight_list[indx]
            current_knapsack_value += values_list[indx]
            removed_values.append(values_list[indx])
            removed_weight.append(weight_list[indx])
            weight_list.pop(indx)
            val_wei_lst.pop(indx)
            values_list.pop(indx)
        print(f"Current capacity: {current_knapsack_status}")
        print(f"Current knapsack value:{current_knapsack_value}")
        print(f'Weight after {weight_list}\n values: {values_list}\n ratio: {val_wei_lst}')

