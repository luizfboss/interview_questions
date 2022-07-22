# FIRST SOLUTION - By myself

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    arr = [str(x) for x in range(1, n+1)]

    for i in range(len(arr)):
        if int(arr[i]) % 3 == 0 and int(arr[i]) % 5 == 0:
            arr[i] = "FizzBuzz"

        elif int(arr[i]) % 3 == 0:
            arr[i] = "Fizz"

        elif int(arr[i]) % 5 == 0:
            arr[i] = "Buzz"

    return arr

print(fizzBuzz(3)) # [1, 2, 'Fizz'] 
print(fizzBuzz(15)) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


# SOLUTION 2 - FOUND ON THE INTERNET:
# def fizzBuzz(n):
#     return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]