# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
  # Examples
  # high_and_low("1 2 3 4 5")  # return "5 1"
  # high_and_low("1 2 -3 4 5") # return "5 -3"
  # high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    numlist = numbers.split(" ")
    i = 0
    highest = int(numlist[0])
    lowest = int(numlist[0])
    while i < len(numlist):
        numlist[i] = int(numlist[i])
        if numlist[i] > highest:
            highest = numlist[i]
        if numlist[i] < lowest:
            lowest = numlist[i]
        i += 1
    highest = str(highest)
    lowest = str(lowest)
    return  highest+" "+lowest

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))