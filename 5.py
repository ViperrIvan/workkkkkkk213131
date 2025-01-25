subjects = [1, 3, 9]
numbers = []
for i in subjects:
    for j in subjects:
        for a in subjects:
            numbers.append(i*100+j*10+a)
out = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i]+numbers[j]>=550:
            out.append(numbers[i]+numbers[j])
out = set(out)
for elem in out:
    print(elem)
