import random 

r = random.randint(-100,100)

found = False


while found == False :
  
  n = input("type a number: ")
  
  if n > r :
    print("the number is too high.")
  elif n < r :
    print("the number is too low.")
  else : print("invalid number")
