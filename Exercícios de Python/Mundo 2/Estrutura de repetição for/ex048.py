s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        count += 1
        s += c
print(f'\nA soma de todos os {count} termos equivale a {s}')
