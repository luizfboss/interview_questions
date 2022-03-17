from random import seed

# Create a program that stores inputs in a text file, with name, age, and appointment

name = str(input('Your name: '))
age = int(input('Your age: '))
appointment = str(input('Your appointment: '))

with open('file.txt', 'a') as arquivo:
  arquivo.write(f'\nName: {name},  Age: {age}, Appointment: {appointment}')
  