def is_subsequence(x0, y0):
    i, j = 0, 0
    while i < len(x0) and j < len(y0):
        if x0[i] == y0[j]:
            i += 1
        j += 1
    return i == len(x0)
print(is_subsequence("apple", "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxleyyzz"))