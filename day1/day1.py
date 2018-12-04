# Initial setup
input = open('input.txt')
result = 0
frequencies = {0}
part2 = True

# Part 1

for line in input.readlines():

    # Parse input
    op = line[0]
    num = int(line[1:])

    # Appropriately add or subtract from total
    if op == '-':
        result = result - num
    else:
        result = result + num
print('Result Part 1: ', result)

# Part 2

# Reset variables
result = 0
input.close()
input = open('input.txt')

# While we have not yet found the result,
# keep iterating through the frequency changes
while part2:
    for line in input.readlines():
        # Parse input
        op = line[0]
        num = int(line[1:])

        # Appropriately add/subtract from total
        if op == '-':
            result = result - num
        else:
            result = result + num

        # Check the current total: if it has been seen before, we have a result
        if result in frequencies:
            print('Result Part 2: ', result)
            part2 = False
            break

        # If it has not been seen before, add it to the set of values
        else: frequencies.add(result)

    input.close()
    input = open('input.txt')

input.close()