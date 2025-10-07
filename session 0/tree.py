def print_christmas_tree(x):
    for i in range(x):
        print(" " * (x - i - 1) + "*" * (2 * i + 1))
print(print_christmas_tree(10))