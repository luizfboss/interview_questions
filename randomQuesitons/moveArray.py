# Provided an array, move part of the array to organize it.


arr = [5, 6, 7, 8, 1, 2, 3, 4]
output = []
target = 8

index = arr.index(target)

moving = arr[:index + 1]
keeping = arr[1 + index:]

output.append(keeping)
output.append(moving)

for n in keeping:
    output.append(n)
for n in moving:
    output.append(n)

output.remove(keeping)
output.remove(moving)

print(output)