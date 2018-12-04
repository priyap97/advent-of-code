input = open('scratch.txt')
hash = {}
resultset = set()
for line in input.readlines():
    split1 = line.split(' ')
    coordinates = split1[2][:-1].split(',')
    size = split1[3].split('x')
    x = int(coordinates[0])
    y = int(coordinates[1])
    x_size = int(size[0])
    y_size = int(size[1])

    for i in range(x, x + x_size):
        for j in range(y, y + y_size):
            if (i,j) in hash:
                if hash[(i,j)] == 1:
                    resultset.add((i,j))
                hash[(i, j)] = hash[(i, j)] + 1
            hash[(i,j)] = 1

input.close()
input = open('scratch.txt')
for line in input.readlines():
    split1 = line.split(' ')
    coordinates = split1[2][:-1].split(',')
    size = split1[3].split('x')
    x = int(coordinates[0])
    y = int(coordinates[1])
    x_size = int(size[0])
    y_size = int(size[1])

    overlap = False
    for i in range(x, x + x_size):
        for j in range(y, y + y_size):
            if (i,j) in resultset:
                overlap = True

    if not(overlap):
        print(split1[0])
