import numpy as np

image = []
galaxies = []


def expand(image):
    new_image = []
    for line in image:
        if line == list('.' * len(line)):
            new_image.append(line)
        new_image.append(line)
    
    image = new_image.copy()
    image = np.array(image).transpose().tolist()
    new_image = []
    for line in image:
        if line == list('.' * len(line)):
            new_image.append(line)
        new_image.append(line)

    image = new_image.copy()
    image = np.array(image).transpose().tolist()

    return image

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


############# MAIN #############

while True:
    try:
        line = input()
        image.append(list(line))
    except EOFError:
        break

image = expand(image)
for i in range(len(image)):
    for j in range(len(image[i])):
        if image[i][j] == '#':
            galaxies.append((i, j))
print(galaxies)

acm = 0
for i in range(len(galaxies)):
    for j in range(len(galaxies)):
        if i != j:
            dist = distance(galaxies[i], galaxies[j])
            # print(i+1, j+1, dist)
            acm+=dist
acm = acm // 2
print(acm)