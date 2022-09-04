import random
option = True

while option == True: 
  randomnumber1 = random.randint(1,49)
  randomnumber2 = random.randint(1,49)
  randomnumber3 = random.randint(1,49)
  randomnumber4 = random.randint(1,49)
  randomnumber5 = random.randint(1,49)
  randomnumber6 = random.randint(1,49)
  bonusball = random.randint(1,49)

  if randomnumber1 in {randomnumber2,randomnumber3,randomnumber4, randomnumber5, randomnumber6}: #not fuly sure what {} do
    option = True
  else:
    option = False

if option == False:
  print("The winning numbers are: ", randomnumber1, randomnumber2, randomnumber3, randomnumber4, randomnumber5, randomnumber6,"!\n The bonus ball number is: ", bonusball,"!")

  