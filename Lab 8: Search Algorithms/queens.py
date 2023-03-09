
# make a generator
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:] 

def solve_queens(n):
    data = list(range(1, n + 1))
    solutions = []
    for perm in all_perms(data):
        solution = True
        for i in range(len(perm)):
            for x in range(i + 1, len(perm)):
                if abs(i - x) == abs(perm[i] - perm[x]):
                    solution = False
        if solution:
            solutions.append(perm)
    solutions = sorted(solutions)
    return solutions

'''
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    for i in all_perms(data):
        print(i)
'''

if __name__ == "__main__":
    n = int(input("Enter a number of queens: \n"))
    solutions = solve_queens(n)
    print(f"The {n}-queens puzzle has {len(solutions)} solutions:")
    for solution in solutions: 
        print(solution)
