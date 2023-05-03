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


if __name__ == "__main__":
    MAX_CAPACITY = 750
    current_knapsack_status = 0
    current_knapsack_value = 0
    removed_values = []
    removed_weight = []
    indx_to_remove = []
    final_candidates = []
    values_list = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
    weight_list = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    while current_knapsack_status + min(weight_list) < MAX_CAPACITY or sum(removed_weight) > MAX_CAPACITY:
        val_wei_lst = create_value_weight_ratio(values_list, weight_list)
        smaller_sets = divide_to_smaller_set(val_wei_lst, 3)
        candidates = choose_best_ratio(smaller_sets)
        print(f"Smaller sets {smaller_sets}")
        for element in candidates:
            indx = find_element_in_main_set(element, val_wei_lst)
            if weight_list[indx] + current_knapsack_status > MAX_CAPACITY:
                print(f"Candidates weight: {removed_weight}\n Values: {removed_values}\n Current knapsack value:{current_knapsack_value}\n Current capacity: {current_knapsack_status}")
                break
            current_knapsack_status += weight_list[indx]
            current_knapsack_value += values_list[indx]
            removed_values.append(values_list[indx])
            removed_weight.append(weight_list[indx])
            final_candidates.append(element)
            weight_list.pop(indx)
            val_wei_lst.pop(indx)
            values_list.pop(indx)
    print(f"Candidates weight: {removed_weight}\n Values: {removed_values}\n Current knapsack value:{current_knapsack_value}\n Current capacity: {current_knapsack_status}")
