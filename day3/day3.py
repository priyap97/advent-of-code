input = open('input.txt')
hash = {}
resultset = set()

# Part 1
for line in input.readlines():
    # Parse input
    split1 = line.split(' ')
    coordinates = split1[2][:-1].split(',')
    size = split1[3].split('x')
    x = int(coordinates[0])
    y = int(coordinates[1])
    x_size = int(size[0])
    y_size = int(size[1])

    # For each square inch in a claim, if it already has been used in another claim we add to resultset
    for i in range(x, x + x_size):
        for j in range(y, y + y_size):
            if (i,j) in hash:
                if hash[(i,j)] == 1:
                    resultset.add((i,j))
                hash[(i, j)] = hash[(i, j)] + 1
            hash[(i,j)] = 1

# Result Part 1
print('Result Part 1', len(resultset))
input.close()

# Result Part 2
input = open('input.txt')
for line in input.readlines():
    # Parse input
    split1 = line.split(' ')
    coordinates = split1[2][:-1].split(',')
    size = split1[3].split('x')
    x = int(coordinates[0])
    y = int(coordinates[1])
    x_size = int(size[0])
    y_size = int(size[1])

    # Search each square inch in a claim
    # If it is in resultset then we know it cannot be the answer, so we set overlap to True
    overlap = False
    for i in range(x, x + x_size):
        for j in range(y, y + y_size):
            if (i,j) in resultset:
                overlap = True

    # If overlap is False, print the claim number
    if not(overlap):
        print('Result Part 2: ', split1[0])
        break