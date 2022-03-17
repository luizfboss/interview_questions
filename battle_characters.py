# Groups of characters decided to make a battle. Help them to figure out which group is more powerful. Create a function that will accept 2 strings and return the one who's stronger.

# Rules:
# Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26;
# Strings will consist of uppercase letters only;
# Only two groups to a fight;
# Group whose total power (A + B + C + ...) is bigger wins;
# If the powers are equal, it's a tie;

def battle(x, y):
    lhs, rhs = fitness(x), fitness(y);
    if lhs>rhs: return x
    elif lhs<rhs : return y
    return "Tie!"
    
def fitness(z):
    return sum(ord(i)-64 for i in z if i.isupper())

print(battle("AAA", "Z"))
print(battle("ONE", "TWO"))
print(battle("ONE", "NEO"))
print(battle("FOUR", "FIVE"))
