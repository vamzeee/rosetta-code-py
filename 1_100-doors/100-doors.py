# https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/100-doors

# As all the doors are closed at the beggining, the only doors that would be open by the end would
# the doors that are interacted with an odd amount of times.
# Amount of times a door is interacted with = number of factors that number has.
# The only numbers that have odd number of factors -> perfect squares (for example, 25's factors are 25, 1 and 5)

counter = 1
output = []
while(counter*counter <= 100) :
    output.append(counter*counter)
    counter+=1
print(output)

# output = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]