in_file = open('input_3.txt', 'r')
# in_file = open('test_3.txt', 'r')

res = 1
terrain = list(map(lambda x: x.rstrip(), in_file.readlines()))

def calc(slope):
    current_y = 0
    val = 0
    for lineIdx in range(0, len(terrain), slope[1]):
        line = terrain[lineIdx]
        if line[current_y] == '#': val += 1
        current_y += slope[0]
        if current_y >= len(line) - 1: current_y -= len(line)
    return val

slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]
for s in slopes:
    res *= calc(s)
print(res)