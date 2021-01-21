print("Quiz")

# Importing packages
import random

# Declaring variables

count1 = 0  #Variable to count score
demoList = []
score = 0   #varaible to store result
name = input("\nEnter player's name :")


def Declaring_result(score,name):
    print()
    print(name,", your score is :",score)

def check(i, answer, count1):
    """

    :type count: object
    """

    # Checking answers
    if i == 0:
        if answer == 'c' or answer == 'C':
            count1 += 1


    if i == 1:
        if answer == 'd' or answer == 'D':
            count1 += 1

    if i == 2:
        if answer == 'b' or answer == 'B':
            count1 += 1

    if i == 3:
        if answer == 'b' or answer == 'B':
            count1 += 1

    if i == 4:
        if answer == 'c' or answer == 'C':
            count1 += 1

    if i == 5:
        if answer == 'a' or answer == 'A':
            count1 += 1

    if i == 6:
        if answer == 'b' or answer == 'B':
            count1 += 1

    if i == 7:
        if answer == 'd' or answer == 'D':
            count1 += 1

    if i == 8:
        if answer == 'c' or answer == 'C':
            count1 += 1

    if i == 9:
        if answer == 'b' or answer == 'B':
            count1 += 1

    return count1  #returning value of count for declaring result


def question(i, count1):

    # Asking questions
    if i == 0:
        print("\nWhat is the capital city of America?")
        print("A : Chicago.IL")
        print("B : New York.NY")
        print("C : Washington,DC")
        print("D : Los Angeles,CA")

    elif i == 1:
        print("\nWho was the first American president?")
        print("A : Thomas jefferson")
        print("B : Abraham lincoln")
        print("C : John Adams")
        print("D : George Washington")

    elif i == 2:
        print("\nIn which city is the Empire State Building located?")
        print("A : Washington,DC")
        print("B : New York,NY")
        print("C : Seattle,WA")
        print("D : Dallas,TX")

    elif i == 3:
        print("\nWhat is the capital city of Louisana?")
        print("A : New Orleans")
        print("B : Baton Rouge")
        print("C : Shreveport")
        print("D : Lafayette")

    elif i == 4:
        print("\nWhen was the declaration of independence?")
        print("A : July 4,1774")
        print("B : July 6,1778")
        print("C : July 4,1776")
        print("D : July 6,1774")

    elif i == 5:
        print("\nWhat is the most populated state in America??")
        print("A : California")
        print("B : ILLionis")
        print("C : Texas")
        print("D : Florida")

    elif i == 6:
        print("\nWhat is the second most spoken language in America?")
        print("A : Chinese")
        print("B : Spanish")
        print("C : Italian")
        print("D : French")

    elif i == 7:
        print("\nWhat is the smallest state of America?")
        print("A : New Jersey")
        print("B : Delaware")
        print("C : Connecticut")
        print("D : Rhode Island")

    elif i == 8:
        print("\nWhat state is the Liberty Bell located in?")
        print("A : New York")
        print("B : Illinois")
        print("C : Pennsylvania")
        print("D : Massachusets")

    elif i == 9:
        print("\nHow many stars are displayed in American flag?")
        print("A : 52")
        print("B : 50")
        print("C : 51")
        print("D : 48")

    #asking for answers from user
    answer = input("\nEnter your option : ")

    #preeventing user from entering input other than given options
    answers=['a','b','c','d','A','B','C','D']
    if answer not in answers:
        answers = input("Choose from above options : ")

    # Calling check functions to check the answers

    return check(i, answer, count1)  #returning scores


for i in range(10):

    # Algorithm for asking random questions everytime
    num = random.randint(0, 9)

    for j in range(100):

        if num in demoList:
            num = random.randint(0, 9)
        else:
            break

    demoList.append(num)

    # calling question() functions
    result = question(num, count1)
    score += result


#Declaring result
Declaring_result(score,name)
