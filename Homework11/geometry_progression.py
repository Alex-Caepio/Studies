def geometric_progression(a, r, n):
    current_term = a
    for _ in range(n):
        yield current_term
        current_term *= r


a = 2
r = 3
n = 5

for term in geometric_progression(a, r, n):
    print(term)
