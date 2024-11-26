import random

score = 0
num = random.randint(1,100)
def guess():
    global score
    attempt = int(input("Enter the number: "))
    if attempt == num:
        score +=1
        print("Correct!")
        print(f"No. of tries: {score}")
    elif attempt > num:
        score += 1
        print("Your number is high")
        guess()
    else:
        score += 1
        print("Your number is low")
        guess()

guess()
a=score
print(f"Your score is {a}")
with open("theperfguess.txt") as f:
    hiscore = f.read()
if hiscore !=  "":
    hiscore = int(hiscore)
else:
    hiscore = 100
print(f"Your hiscore is {hiscore}")
with open("theperfguess.txt","w")as f:
    if a<hiscore:
        print("Your hiscore is broken")
        f.write(str(a))
    else:
        f.write(str(hiscore))
