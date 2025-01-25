from itertools import permutations
numbers = [1, 3, 7]
combinations = list(permutations(numbers))
for i in range(6):
    print(str(combinations[i]).replace(',','').replace(')','').replace('(',''))
print(len(combinations))
