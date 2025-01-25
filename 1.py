import itertools
subjects = ['музыка', 'математика', 'русский язык', 'литература', 'история']
permutations = list(itertools.permutations(subjects))
for i, perm in enumerate(permutations):
    print(f"Способ {i + 1}: {', '.join(perm)}")
