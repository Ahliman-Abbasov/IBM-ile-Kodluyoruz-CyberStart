x1, y1 = 1, 1
x2, y2 = 4, 5
points = [(x1, y1),
          (x2, y2)]


def euclideanDistance(tup1, tup2):
    return ((tup1[0] - tup2[0]) ** 2 + (tup1[1] - tup2[1]) ** 2) ** (1 / 2)


distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

print(min(distances))
