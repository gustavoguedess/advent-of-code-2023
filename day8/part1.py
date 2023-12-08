import re

network = {}

instructions = input()
input()
while True:
    try:
        line = input()
        
        # format origin = (left, right)
        origin, left, right = re.match(r'(\w+) = \((\w+), (\w+)\)', line).groups()
        network[origin] = {'L': left, 'R': right}
    except EOFError:
        break

steps = 0
current = 'AAA'
while current != 'ZZZ':
    # current = current[instructions[steps%len(instructions)]]
    current = network[current][instructions[steps%len(instructions)]]
    steps += 1
    print(current, instructions[steps%len(instructions)])

print(steps)