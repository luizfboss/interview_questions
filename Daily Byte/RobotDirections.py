# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.


def RobotDirection(directions):
    count_directions = {"vertical": 0, "horizontal": 0}
    current_directions = [direction for direction in directions]

    for command in current_directions:
        if command == "U":
            count_directions["vertical"] += 1
        elif command == "D":
            count_directions["vertical"] -= 1
        elif command == "L":
            count_directions["horizontal"] -= 1
        elif command == "R":
            count_directions["horizontal"] += 1

    if count_directions["horizontal"] == 0 and count_directions["vertical"] == 0:
        return True
    return False


print(RobotDirection("LR")) # return True
print(RobotDirection("URURD")) # return False
print(RobotDirection("RUULLDRD")) # return True
print(RobotDirection("DDUDLLRRL")) # return False
print(RobotDirection("DDUDLULURDLRRU")) # return True