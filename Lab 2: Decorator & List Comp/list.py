def list_comprehension(x):
    return [x[i] + x[i-1] for i in range(1, len(x), 1)]
