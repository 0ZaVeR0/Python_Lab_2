def f(a, val):
  return min((x for x in a if x > val), default=None)

a = [1, 2, 5, 22, 33, 44, 312]
print(f(a, 6))
print(f(a,10))
print(f(a, 1000))