ages = input().split()
ages_True = filter(lambda x: 18 <= int(x) <= 35,ages)
print(*ages_True)