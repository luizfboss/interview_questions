# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
# Given a year, return the century it is in.


# Solution 1:
def century(year):
  century = 0
  if year % 100 == 0:
      century = year / 100
  else:
      century = (year // 100) + 1
  return century

# Solution 2:
def century(year):
    return (year + 99) // 100