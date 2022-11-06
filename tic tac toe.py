import random
number=base = ["1","2","3","4","5","6","7","8","9"]
box = "___________\n|1 | 2 | 3|\n|_________|\n|4 | 5 | 6|\n|_________|\n|7 | 8 | 9|\n|_________|"
compnum=em=playernum = []
pc= "COMPUTER"
user = "USER"
start = random.choice(base)
start = int(start)
def ender(ids):
    print(ids," WIN ")
    exitf = input("press enter to exit")
    exit()

def playnum1(box):
    if ((("1" in playernum) and ("2" in playernum) and ("3" in playernum)) or (("4" in playernum) and ("5" in playernum) and ("6" in playernum)) or (("7" in playernum) and ("8" in playernum) and ("9" in playernum)) or (("1" in playernum) and ("4" in playernum) and ("7" in playernum)) or(("2" in playernum) and ("5" in playernum) and ("8" in playernum)) or(("9" in playernum) and ("6" in playernum) and ("3" in playernum)) or (("1" in playernum) and ("5" in playernum) and ("9" in playernum)) or (("7" in playernum) and ("5" in playernum) and ("3" in playernum))):
              print(box)
              ender(user)
    

def playpc1(box):
    if ((("1" in compnum) and ("2" in compnum) and ("3" in compnum)) or (("4" in compnum) and ("5" in compnum) and ("6" in compnum)) or (("7" in compnum) and ("8" in compnum) and ("9" in compnum)) or (("1" in compnum) and ("4" in compnum) and ("7" in compnum)) or(("2" in compnum) and ("5" in compnum) and ("8" in compnum)) or(("9" in compnum) and ("6" in compnum) and ("3" in compnum)) or (("1" in compnum) and ("5" in compnum) and ("9" in compnum)) or (("7" in compnum) and ("5" in compnum) and ("3" in compnum))):
              print(box)
              ender(pc)  
              

def player(box):
  i = 1
  while (i < 11): 
    if (number == []):
         playnum1(box)
         playpc1(box)
         print("no moves left")
         break
    player = input(box)
    if (player in base):
      if (player in em):
        print(box)
        print("no option try again")
      else:
        playernum.append(player)
        em.append(player)
        number.remove(player)
        box = box.replace(player,"X")
        playnum1(box)
        if (number == []):
          print(box)
          print("no moves left")
        comp = random.choice(number)
        compnum.append(comp)
        em.append(comp)
        number.remove(comp)
        box = box.replace(comp,"O")
        playpc1(box)
    else:
       print("error")   

def comp(box):
    comp = random.choice(number)
    compnum.append(comp)
    em.append(comp)
    number.remove(comp)
    box = box.replace(comp,"O")
    a = 1
    while (a< 11):
       playpc1(box)          
       if (number == []):
         playnum1(box)
         break 
         playpc1(box) 
         print("no moves left")
         break
       else:
         player = input(box)
         if (player in base):
           if (player in em):
              print(box)
              print("no option try again")
           else:
              playernum.append(player)
              em.append(player)
              number.remove(player)
              box = box.replace(player,"X")
              playnum1(box)
              comp = random.choice(number)
              compnum.append(comp)
              em.append(comp)
              number.remove(comp) 
              box = box.replace(comp,"O")
         else:
            print("error") 
            
if ((start%2) == 0):
  player(box)
else:
  comp(box)