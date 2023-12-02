import re

f = open("data_1.txt","r")

red = 12
green = 13
blue = 14


lines = f.readlines()
line = lines[2]       # only change this index for line
game_id = line.split(':')
game_id2 = game_id[0].split('Game ', 1)
game = game_id2[1] # always index 1

rolls = game_id[1].split(';')
roll_1 = rolls[0]
roll_2 = rolls[1]
roll_3 = rolls[2]

print (game)
print(roll_1)

print(roll_1.split(' blue',1))
#test = roll_1.split(' blue',1)

if "blue" in roll_1:
    print("yesyes")
    print
    test = roll_1.split(' blue')
    test = int(test[0])
else:
    test = 0
    print("nono")

if test > blue:
    game = 0

print(game)



