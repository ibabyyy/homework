"""Hi das Spiel heist Fizz Buzz!!! Ich erkläre es dir kurz...

Ich zähle von 1 aufäwrts,
ist die Zahl durch 3 teilbar, gib Fizz ein,
ist die Zahl durch 5 teilbar, gib Buzz ein,
ist die Zahl durch 3 und 5 teilbar, gib FizzBuzz ein,
ist die Zahl nicht durch 3 oder 5 teilbar drückst du einfach Enter.
"""






for i in range(1,99999):
    
    if i % 3 == 0:
        if i % 5 == 0:
            print(i)
            fizzbuzz = input()
            if fizzbuzz == "fizzbuzz":
                continue
            else:
                print("haha verloren")
        else:
            print(i)        
        if input() == "fizz":
            continue
        else: 
            print("haha verloren")
            break

    elif i % 5 == 0:
        print(i)
        if input() == "buzz":
            continue
        else:
            print("haha verloren")
            break




    else:
        print(i)
        input()
        continue



## import math

# startzahl = 1
# print(startzahl)

# while startzahl<=100000000000000:
#     a = input()
#     a == "FizzBuzz"
#     b = input()
#     b == "Fizz"
#     c = input()
#     c == "Buzz"
#     d = input()
#     d == ""

#     while startzahl % 3 == 0 and startzahl % 5 == 0 and input() == a:
#         print(startzahl)
#         break
#     while   startzahl % 3 == 0 and input() == b:
#         print(startzahl)
#         break
#     while startzahl % 5 == 0 and input() == c:
#         print(startzahl)
#         break
#     while startzahl % 3 != 0 or startzahl % 5 != 0 and input() == "":
#         print(startzahl)
#         break
#     startzahl=startzahl+1
#     break


#print(startzahl)

# def game():
#     userinput = input()
#     startzahl = 0
#     startzahl +=1

#     if startzahl % 3 == 0 and startzahl % 5 == 0 and input() == "FizzBuzz":
#         print(startzahl)
#     elif startzahl % 3 == 0 and input() == "Fizz":
#         print(startzahl)
#     elif startzahl % 5 == 0 and input() == "Buzz":
#         print(startzahl)
#     elif startzahl % 3 != 0 or startzahl % 5 != 0 and input() == "":
#         print(startzahl)
    



#print(1) 


#while (startzahl % 3 and 5 == 0 and input() == "FizzBuzz") or (startzahl % 3 == 0 and input() == "Fizz") or (startzahl % 5 == 0 and input() == "Buzz") or (startzahl % 3 != 0 or startzahl % 5 != 0 and input() == ""):
    #print(startzahl+=1)
    #else: 
    #print("u lost")