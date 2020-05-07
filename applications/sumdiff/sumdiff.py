"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def sum_diff(q_set, cb):
    # Here, we cache the results of function `cb` for later.
    cb_cache = {}
    for item in q_set:
        cb_cache[item] = cb(item)
    print(f"callback function cache: {cb_cache}")
    print("Finished caching callback results.")

    # Cache the results of every possible sum combo.

    sum_cache = {}

    # for (number1, product1) in cb_cache.items():
    #     for (number2, product2) in cb_cache.items():
    #         if (number1, number2) not in sum_cache.keys() and (number2, number1) not in sum_cache.keys():
    #             sum_cache[(number1, number2)] = product1 + product2

    for (number1, product1) in cb_cache.items():
        for (number2, product2) in cb_cache.items():
            current_sum = product1 + product2
            if current_sum not in sum_cache.keys():
                sum_cache[current_sum] = [(number1, number2)]
            elif current_sum in sum_cache.keys():
                sum_cache[current_sum].append((number1, number2))

    print(f"sum cache: {sum_cache}")
    print("Finished caching sums.")

    # Cache the results of every possible difference combo.
    diff_cache = {}

    # for (number1, product1) in cb_cache.items():
    #     for (number2, product2) in cb_cache.items():
    #         if (number1, number2) not in sum_cache.keys() and product2 < product1:
    #             diff_cache[(number1, number2)] = product1 - product2
    #         elif (number2, number1) not in sum_cache.keys() and product1 < product2:
    #             diff_cache[(number2, number1)] = product2 - product1

    for (number1, product1) in cb_cache.items():
        for (number2, product2) in cb_cache.items():
            current_diff = product1 - product2
            if current_diff not in diff_cache.keys():
                diff_cache[current_diff] = [(number1, number2)]
            elif current_diff in diff_cache.keys():
                diff_cache[current_diff].append((number1, number2))

    print(f"diff cache: {diff_cache}")
    print("Finished caching diffs.")

    combinations = {}

    for product in sum_cache.keys():
        if product in diff_cache.keys():
            combinations[product] = (sum_cache[product], diff_cache[product])

    print(f"combinations: {combinations}")


sum_diff(q, f)
