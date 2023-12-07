fp = 'input.txt'
with open(fp, 'w') as f:
    for i in range(1, 13):
        for j in range(1, 13):
            f.write(f'{i} × {j}\t{i*j}\n')

