# Initial setup
input = open('input.txt')
twos = set()
threes = set()

# Part 1

for line in input.readlines():
    # Make an empty hash that will store the letters
    # and counts of each time they appear in the line
    hash = {}
    line = line.strip()
    for char in line:
        if char in hash:
            hash[char] = hash[char] + 1
        else:
            hash[char] = 1
    # if any character appears twice, add to the set with 2s
    # if any character appears thrice, add to the set with 3s
    for key in hash.keys():
        if hash[key] == 2:
            twos.add(line)
        if hash[key] == 3:
            threes.add(line)

# Output results
print('Result Part 1: ', len(twos)*len(threes))

# Part 2

# Helper function
# Compute hamming distance between 2 strings of equal length
def hammingdist(x,y):
    dist = 0
    for char1, char2 in zip(x,y):
        if char1 != char2:
            dist = dist + 1
    return dist

# Setup
input.close()
input = open('input.txt')
lines = input.readlines()
found = False
result1 = ''
result2 = ''

# Iterate through IDs and find hamming distances
for x in range(len(lines)):
    hash = {}
    line = lines[x]
    line = line.strip()

    # Compute hamming distance with all succeeding inputs
    # If distance of 1 is found, save result and stop
    for y in range(x+1, len(lines)):
        line2 = lines[y]
        if hammingdist(line, line2) == 1:
            result1 = line
            result2 = line2
            found = True
            break
    if found: break

# Output result by printing everything minus the unmatching char
resultzip = ''
for char1, char2 in zip(result1, result2):
    if char1 == char2:
        resultzip = resultzip + char1

print('Result Part 2: ', resultzip)
