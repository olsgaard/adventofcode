def rotate(f, by):
    dir = by[0]
    i = int(by[1:])
    if dir == "L":
        return (f-i)%100
    if dir == "R":
        return (f+i)%100

def run(input):
    pos = 50
    z = 0
    for line in input.split('\n'):
        pos = rotate(pos, line.strip())
        z = z+1 if pos == 0 else z
    return z

test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

print(run(test))
with open("day01.txt", "r") as f:
    puzzle = f.read().strip()
    print(run(puzzle))

