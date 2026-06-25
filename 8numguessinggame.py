# guess the number
import random

choosen_num=random.randint(1,100)
def makeguess(attempts):
        attempt=attempts
        while attempt > 0:
              print(f"You have {attempt} attempts")
              global choosen_num
              guess=int(input("Make a guess :"))
              if guess==choosen_num:
                  print("Correct☑️\nYou won!!🏅")
                  break
              elif guess>choosen_num:
                  print("high⬆")
                  attempt-=1

              elif guess<choosen_num:
                  print("low⬇")
                  attempt-=1
        if attempt ==0:
          print(f"You lose!!😔\nThe correct number is {choosen_num}")  

    
    

while True:
    easy=10
    hard=5
    print(" ")
    print("Welcome to my number guessing game!!")
    print(" ")

    level=input("Choose a difficulty level: ")
    
    if level=="easy":
        makeguess(easy)
        break
    elif level=="hard":
        makeguess(hard)

        break
    else:
        print ("Choose between easy of hard!! ")
        continue

        