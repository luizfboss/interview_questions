# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
      if pin.isnumeric():
        if len(pin) != 4 and len(pin) != 6:
            return False
        elif '-' in pin and '.' in pin:
            return False
        return True
      return False



print(validate_pin("1")) # False
print(validate_pin("12")) # False
print(validate_pin("123")) # False
print(validate_pin("12345")) # False
print(validate_pin("1234567")) # False
print(validate_pin("-1234")) # False
print(validate_pin("-12345")) # False
print(validate_pin("1.234")) # False
print(validate_pin("00000000")) # False

print("\n\n")

print(validate_pin("1234")) # True
print(validate_pin("0000")) # True
print(validate_pin("1111")) # True
print(validate_pin("123456")) # True
print(validate_pin("098765")) # True
print(validate_pin("000000")) # True
print(validate_pin("123456")) # True
print(validate_pin("090909")) # True