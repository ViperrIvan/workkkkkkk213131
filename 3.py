from itertools import permutations
import math
numbersPart1 = [4, 7, 6]
numbersPart2 = [4, 3, 6]

combinations = list(permutations(numbersPart1))
for elem in combinations:
    print(str(elem).replace(')','').replace('(','').replace(',',''), '3')
combinations = list(permutations(numbersPart2))
for elem in combinations:
    print(str(elem).replace(')','').replace('(','').replace(',',''), '7')
