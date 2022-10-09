import random, time


def solve_knapsack(val, weights, capacity):
    actual_capacity = 0
    actual_capacity_arr = []
    actual_profit = 0
    actual_profit_arr = []
    while actual_capacity <= capacity:
        choosen = random.randint(0, len(val))
        if actual_capacity + weights[choosen] >= capacity:
            print(f"Final profit is {actual_profit}\n Final weight is {actual_capacity}")
            return
        actual_capacity = actual_capacity + weights[choosen]
        actual_profit = actual_profit + val[choosen]
        actual_capacity_arr.append(actual_capacity)
        actual_profit_arr.append(actual_profit)
        val.pop(choosen)
        weights.pop(choosen)
        print(f"Actual profit is {actual_profit} \nActual weight is {actual_capacity}")
    print(f"Final profit is {actual_profit}\n Final weight is {actual_capacity}")


if __name__ == "__main__":
    value = [44, 103, 105, 50, 86, 89, 125, 102, 76, 40, 4, 43, 79, 109, 64, 23, 119, 65, 116, 73, 58, 47, 34, 78, 71,
             71, 3, 67, 21, 17, 3, 16, 86, 118, 83, 67, 2, 7, 17, 79, 27, 113, 43, 20, 86, 14, 15, 111, 27, 35, 112, 97,
             84, 59, 15, 82, 78, 111, 73, 54, 12, 4, 9, 106, 4, 13, 22, 59, 48, 96, 90, 7, 116, 96, 77]
    weight = [166, 260, 233, 365, 304, 91, 272, 224, 283, 116, 237, 61, 275, 311, 323, 366, 292, 221, 114, 347, 207,
              366, 299, 240, 145, 137, 257, 270, 96, 313, 93, 336, 196, 79, 84, 185, 343, 253, 280, 185, 198, 263, 269,
              256, 17, 220, 196, 364, 229, 16, 372, 30, 56, 26, 11, 339, 103, 63, 295, 215, 204, 310, 220, 66, 191, 201,
              297, 100, 253, 331, 24, 59, 67, 206, 76]
    max_capacity = 750
    for i in range(5):
        start = time.time_ns()
        solve_knapsack(value, weight, max_capacity)
        stop = time.time_ns()
        print(f"Result in {(stop - start)/1000000000} s")