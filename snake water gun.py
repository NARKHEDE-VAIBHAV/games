import random
for i in range(5):
 player = input("Snake(s) Water(w) Gun(g)")
 def game(player):
    num = ("s" , "w" , "g")
    comp = random.choice(num)
    print(f"computer choice {comp}\nyour choice  " + player )
    if (comp == player):
        print("tie")
    elif (comp == "s" and player == "w") or (comp == "g" and player == "s") or (comp == "w" and player == "g"):
       print("COMPUTER WIN")
    else:
       print("PLAYER WIN")
 game(player)