import random
import matplotlib.pyplot as plt


def generate_value(no_items, max_capacity):
    weight = []
    for i in range(no_items):
        weight.append(random.randint(1, int(max_capacity/6)))
    return weight


def generate_weight(no_items, max_capacity):
    value = []
    for i in range(no_items):
        value.append(random.randint(5, int(max_capacity/2)))
    return value


if __name__ == '__main__':
    '''max_cap = 750
    values = generate_value(90, max_cap)
    weight = generate_weight(90, max_cap)
    print(f"Generated values are: {values}\n Generated weights: {weight}")
'''
    time_annealing = [0.094, 1.6499662, 2.0448464, 39.8029987, 46.55890]
    time_dynamic = [1.655 *10**-18, 0.0069998, 0.007399, 0.02299461, 0.239998]
    time_greedy_mvalue = [1.655*10**-18, 0.0046398, 0.0377399, 0.2238015, 0.267072]
    time_greedy_mweight = [1.655*10**-18, 0.0046398, 0.0377399, 0.2238015, 0.267072]
    time_random = [1.655*10**-18, 0.0066938, 0.0046398, 0.3170647, 0.3670725]
    time_brute_force = [0.0100, 0.1690012, 3.8480005, 113.21200, 601.12887]
    no_items = [15, 30, 50, 75, 90]
    plt.semilogy(no_items, time_brute_force, 'red', no_items, time_dynamic, 'blue', no_items, time_annealing, 'magenta')
    plt.legend(['Brute-force', 'Dynamic programming', 'Simulated annealling'])
    plt.grid()
    plt.xlabel('Number of items [n]')
    plt.ylabel('Time [s]')
    plt.title('T(n) Time in function of items - Compare "smart" algorithm')
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
