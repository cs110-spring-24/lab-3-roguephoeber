import random
onec=0
twoc=0
thrc=0
fourc=0
fivec=0
sixc=0
question=int(input("Prompt list: \n 1. Prints out the numbers 1 to 1000. \n 2. Prints out the odd numbers between 1 and 1000. \n 3. Prints out the numbers between 0 and 1000 that are divisible by 3. \n 4. Prints out the numbers between 1 and 1000 that are divisible by 3 or 5. \n 5. Enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200. \n 6. Prints out each letter of a string line by line \n 7. Asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long. \n 8. Rolls 1000 dice and prints out the number of times each number was rolled. \n 9. checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. \n 10. prints out the prime numbers less than 1000. \n Select a prompt: "))
if question == 1:
    for i in range(1,1001):
        print(i)
if question == 2:
    for i in range(1,1001,2):
        print(i)
if question == 3:
    for i in range(0,1001):
        if i%3==0:
            print(i)
if question == 4:
    for i in range(0,1001):
        if i%3==0 or i%5==0:
            print(i)
if question == 5:
    num=int(input("Enter a number greater than 200: "))
    if num < 200:
        print("This number is less than 200, plese enter a number greater than 200.")
        num=int(input("Enter a number greater than 200: "))
    for i in range(1,num):
        if i%11==0 or i%13==0:
            print(i)
string="hello world"
if question==6:
    for i in range(len(string)):
        print(string[i])
if question==7:
    usrstr=input("Enter a string: ")
    for i in range(len(usrstr),2):
        print(i)
if question==8:
    for i in range(1000):
        die=random.randint(1,6)
        if die==1:
            onec+=1
        elif die==2:
            twoc+=1
        elif die==3:
            thrc+=1
        elif die==4:
            fourc+=1
        elif die==5:
            fivec+=1
        else:
            sixc+=1
    print(f"after 1000 rolls, we rolled {onec} one, {twoc} twos, {thrc} threes, {fourc} fours, {fivec} fives, and {sixc} sixes.")
if question==9:
    prime=int(input("Give a number and this will check if it's prime or not. "))
    if prime == 1:
        print("1 is not a prime number.")
    for i in range(2, prime):
        if (prime % i) == 0:
            print(f"{prime} is not a prime number")
            break
        else:
            print(f"{prime} is a prime number")
            break
    
if question==10:
    print("The prime numbers between 1 and 100 are: ")
    for i in range(1, 1001):
        if i > 1:
            for t in range(2, i):
                if (i % t) == 0:
                    break
            else:
                print(i)




    
