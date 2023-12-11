import numpy as np

expand_times = 1000000
image = []
galaxies = []

def get_galaxies(image):
    image_transposed = np.array(image).transpose().tolist()

    ii = 0
    for i in range(len(image)):
        ii += 1
        if image[i] == list('.' * len(image[i])):
            ii += expand_times - 1
        jj = 0
        for j in range(len(image[i])):
            jj += 1
            if image_transposed[j] == list('.' * len(image_transposed[j])):
                jj += expand_times - 1
            if image[i][j] == '#':
                galaxies.append((ii, jj))
    return galaxies

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


############# MAIN #############

while True:
    try:
        line = input()
        image.append(list(line))
    except EOFError:
        break

galaxies = get_galaxies(image)
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