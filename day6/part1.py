import numpy as np

while True:
    try:
        time = list(map(int, input().split(':')[-1].strip().split()))
        distance = list(map(int, input().split(':')[-1].strip().split()))
        print(time)
        print(distance)
    except EOFError:
        break

results = []
for i in range(len(time)):
    ways = 0
    for j in range(1,time[i]):
        if (time[i]-j)*j > distance[i]:
            ways += 1
    results.append(ways)
print(results)

print(np.prod(results))