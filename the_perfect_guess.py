import random
r = random.randint(1, 100)
g = 0
cnt = 0
print("enter ur first guess\n")
while(r != g):
   g =  int(input())
   cnt = cnt + 1
   if(g > r):
       print("lower number please!")
   if(g < r):
       print("higher number please!")
   if(g == r):
       print(f"You guessed the number in {cnt} guesses.")


