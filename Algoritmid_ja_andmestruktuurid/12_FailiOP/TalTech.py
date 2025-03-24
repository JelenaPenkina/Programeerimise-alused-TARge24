with open('numbers.txt') as f:
    lines = f.read(3)
    print(lines)

with open('results.txt', 'w') as f:
    f.write('1')
    f.writelines(['ago', 'rida', 'end'])