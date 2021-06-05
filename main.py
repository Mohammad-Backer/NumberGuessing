import random as rand

def multiple(rannumb, *args):
    c = 0
    i = 1
    mult = []
    while c<1000:
        c = rannumb * i
        mult.append(c)
        i += 1
    print("\nOne of its multiples is : ", rand.choice(mult))
    

def divisible(rannumb, *args):
    divis = []
    for i in range(1,101):
        if rannumb % i == 0:
            divis.append(i)
    print("\nIt is divisible by", rand.choice(divis))
    

def comparision(rannum, num = 50):
    if rannum >= num:
        print("\nIt is greater or equal to: " + str(num))
    else:
        print("\nit is smaller than: " + str(num))

def hints(numb, limit = 50):
    randNumbHints = rand.randint(0,3)
    hintDict = {
        1:multiple,
        2:divisible,
        3:comparision,
    }
    li = []
    hint = []
    for i in range(0,randNumbHints):
        a = rand.randint(1,3)
        if a not in li:
            li.append(a)
            hint.append(hintDict[a](numb, limit))
    return hint

def main():
    
    print("The computer chose a number between 0 and 100 can you guess it ?")
    randNumber = rand.randint(0,100)
    print("Here are the hints: ")
    hints(randNumber)
    isNotcorrect = True
    score = 100
    while isNotcorrect:
        try:
            guess = int(input("Your guess is ? "))
            if guess >= 0 and guess <= 100:
                if guess == randNumber:
                    print("You have guessed correctly!\n The number is :  " + str(randNumber))
                    if score>0:
                        print("\nYour score is: ",str(score))
                    elif score <=0:
                        print("\nYour score is 0! You guessed it in more then 10 times!")
                    isNotcorrect = False
                else: 
                    print("Try again!")
                    score -= 10
                    hints(randNumber, guess)
            else:
                print("Please Enter a number between 0 and 100!")
        except Exception:
                print("Please Enter a number between 0 and 100!")

if __name__ == '__main__':
    main()
