# print('TBA done..')

def ratio_choice(max_capacity, weight, value, n):
    ratio = []
    actual_capacity = 0
    final_weight = []
    final_profit = []
    for element in range(0, n):
        ratio.append(value[element] / weight[element])
    # print(ratio.index(max(ratio)))##index
    # print(ratio[ratio.index(max(ratio))])##value
    while actual_capacity <= max_capacity:
        if actual_capacity + ratio[ratio.index(max(ratio))] <= max_capacity:
            index = ratio.index(max(ratio))
            actual_capacity += weight[index]
            final_weight.append(weight[index])
            final_profit.append(value[index])
            ratio.pop(index)
            weight.pop(index)
            value.pop(index)
    final_profit.pop(len(final_profit) - 1)
    final_weight.pop(len(final_weight) - 1)
    print(f"Final weight: {final_weight} and sum is {sum(final_weight)}")
    print(f"Final profits {final_profit} and sum is {sum(final_profit)}")


value = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240, 50]
weight = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120, 1]
max_capaxity = 750
ratio_choice(max_capaxity, weight, value, len(value))
