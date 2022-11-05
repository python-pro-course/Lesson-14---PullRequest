s = input().split()

print((*map(lambda x: (*x.split('-'),), s),))