import random
rand=random.randint(1,100)
c=0
user=None
while(user!=rand):
    user=int(input("Enter your guess(1-100): "))
    if(user==rand):
        print("YOU GUESSED IT RIGHT")
    elif user>rand:
        print("YOU GUESSED IT WRONG,TRY SMALLER VALUES")
    else:
        print("YOU GUESSED IT WRONG,TRY BIGGER VALUES")
    c+=1
    

print(f"YOU GUESSED IT RIGHT IN {c} attempts")
with open("hs.txt","r") as f:
    hs=int(f.read())
if(c<hs):
    print("MY MY! THAT IS THE BEST SCORE I HAVE GOT")
    with open("hs.txt","w") as f:
        f.write(str(c))
