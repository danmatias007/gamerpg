
import random
import time



name = input("What is your name?\n>>>")

pacote = ["demonic eye","goblin","slime","zombie","spider","skeleton","dragon","chimera"]

chosenmonster = random.choice(pacote)

print(" ")
print("an {} appeared!".format(chosenmonster))
print(" ")
player = 100
monster = 100

#Your attack

while player > 1:
  time.sleep(1)
  print("==================")
  print(" ")
  print("{}'s life: {}\n{}'s life: {}".format(name, player, chosenmonster, monster))
  print(" ")
  time.sleep(1)
  print("What {} will do?".format(name))
  attack= int(input("[1] Normal attack\n[2] Special attack\n[3] Recover life\n>>>"))
  print(" ")
  
  if attack == 1:
    time.sleep(1)
    print("{} dealt 15 damage!".format(name))
    monster = monster - 15
    time.sleep(1)
    print("{} have {} life now!".format(chosenmonster, monster))
    print(" ")
    
  elif attack == 2:
    time.sleep(1)
    chance = random.randint(1,2)
  
    if chance == 1:
      print("{} dealt 35 damage!".format(name))
      monster = monster - 35
      time.sleep(1)
      print("{} have {} life now!".format(chosenmonster, monster))
      print(" ")
      
    else:
      print("{} failed!".format(name))
      
  elif attack == 3:
    time.sleep(1)
    print("{} recovered 30 life!".format(name))
    time.sleep(1)
    player = player + 30
    print("{} have {} life now!".format(name, player))
    
    #Win or lose
    
  if player < 1:
    time.sleep(1)
    print("{} lose...".format(name))
    time.sleep(2)
    break
    
  elif monster < 1:
    time.sleep(1)
    print("{} wins!!".format(name))
    time.sleep(2)
    break
    
    #enemy attack
  
  print("==================")
  print(" ")
  print("{} time!".format(chosenmonster))
  time.sleep(2)
  print(" ")
  
  enemyattack = random.randint(1,3)
  
  if enemyattack == 1:
    print("{} dealt 10 damage!".format(chosenmonster))
    player = player - 10
    time.sleep(1)
    print("{} have {} life now!".format(name, player))
    print(" ")
  
  elif enemyattack == 2:
    print("{} dealt 15 damage!".format(chosenmonster))
    player = player - 1
    time.sleep(1)
    print("{} have {} life now!".format(name, player))
    print(" ")
    
  elif enemyattack == 3:
    print("{} dealt 20 damage!".format(chosenmonster))
    player = player - 20
    time.sleep(1)
    print("{} have {} life now!".format(name, player))
    print(" ")
    
  print(" ")
  
  #win or lose 2
  
  if player < 1:
    time.sleep(1)
    print("{} lose...".format(name))
    time.sleep(2)
    break
    
  elif monster < 1:
    time.sleep(1)
    print("{} wins!!".format(name))
    time.sleep(2)
    break

    