# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    minimum = lst[0]
    maximum = lst[0]
    
    for n in lst:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    return [minimum, maximum]
