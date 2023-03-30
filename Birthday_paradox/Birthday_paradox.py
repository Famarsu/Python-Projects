import random
import math
from statistics import NormalDist
random.seed()

#INPUTS
number_of_people = int(input("number of people: "))
iterations = int(input("iterations: "))
method = input("method (detailed/simple): ")
matches = []
correct = 0

#DEFINITIONS
def check_detailed(kids_birthdays,matches,number_of_people):
    for i in range(0,(number_of_people-1)):
        for j in range(i+1,number_of_people):
            if kids_birthdays[i] == kids_birthdays[j]:
                matches.append(kids_birthdays[i])
    return matches

def check_simple(kids_birthdays,matches,number_of_people):
    for i in range(0,(number_of_people-1)):
        for j in range(i+1,number_of_people):
            if kids_birthdays[i] == kids_birthdays[j]:
                matches.append(kids_birthdays[i])
                return matches
    return matches
                

#PLAY
for k in range(0,iterations):
    #SET-UP
    kids_birthdays = tuple(i+random.randint(1,365)-i for i in range(0, number_of_people))
    matches = [0] 
    if method == "detailed":
        matches = check_detailed(kids_birthdays,matches,number_of_people)
    elif method =="simple":
        matches = check_simple(kids_birthdays,matches,number_of_people)
    else:
        print("Incorrect method")
    if len(matches) > 1:
        correct += 1

""" #RESULT
print("There have been " + str(len(matches)) + " matches. They are: " + str(matches)) """
        

#STATISTICS
probability = (correct/iterations)
standard_error = (math.sqrt((probability)*(1-(probability))/iterations))
sigmas = (NormalDist().inv_cdf(1-standard_error))
print("The paradox happens with a " + str(probability) + " probability")
print("Standard error is " + str(standard_error))
print("The result has " + str(sigmas) + " sigmas")