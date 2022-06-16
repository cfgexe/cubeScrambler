import random
scram_len = input("How many moves long?: ")
if scram_len == "":
    scram_len = 15
moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
scram = ""
for i in range(0, int(scram_len)):
    random_move = random.randint(0, len(moves) - 1)
    	
    if i > 0:
    	while moves[random_move][0] == prev_move[0]:
    	    random_move = random.randint(0, len(moves) - 1)
    scram += " " + moves[random_move]
    prev_move = moves[random_move]
print(scram)
