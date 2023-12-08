import re
import time
import numpy 

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

node = []
for key in network:
    if key.endswith('A'):
        node.append(key)
print(' '.join(node))
start = node.copy()

start_cycle = [0 for _ in range(len(node))]
cycle = start_cycle.copy()

steps = 0
while not all([x.endswith('Z') for x in node]):
    # current = current[instructions[steps%len(instructions)]]
    node = list(map(lambda current: network[current][instructions[steps%len(instructions)]], node))
    
    

    condition = True
    for i in range(len(node)):
        if node[i].endswith('Z'):
            if start_cycle[i] == 0:
                start_cycle[i] = steps+1
            elif cycle[i] == 0:
                cycle[i] = steps - start_cycle[i]+1

    node_print = list(map(lambda x: '\033[91m'+x+'\033[0m' if x.endswith('Z') else x, node))
    print(steps, instructions[steps%len(instructions)], ' '.join(node_print), start_cycle, cycle)
    
    if all(cycle):
        break
    steps += 1

current = start_cycle.copy()
print(current)
print(cycle)

import math
print(math.lcm(*cycle))

# while not all(i==current[0] for i in current):
#     small_index = numpy.argmin(current)
#     current[small_index] += cycle[small_index]
#     print(current)


# print(current[0])
