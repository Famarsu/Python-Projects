import random
import math
from statistics import NormalDist
random.seed()

#INPUTS
number_of_doors=int(input("number of doors: "))
iterations=int(input("iterations: "))
strategy=(input("strategy (stay/change): "))
new_door = 0
correct = 0

#DEFINITIONS
def stay_strategy(picked_door):
    new_door = picked_door
    return new_door


def change_strategy(number_of_doors,picked_door,deleted_door):
    new_door = (random.randint(1,number_of_doors))
    while new_door == picked_door or new_door == deleted_door:
        new_door = (random.randint(1,number_of_doors))
    return new_door

#PLAY
for i in range(1,iterations+1):
    #SET-UP
    correct_door = (random.randint(1,number_of_doors))
    picked_door = (random.randint(1,number_of_doors))
    deleted_door = (random.randint(1,number_of_doors))
    while deleted_door == correct_door or deleted_door == picked_door:
        deleted_door = (random.randint(1,number_of_doors))
    #STRATEGY
    if strategy == "stay":
        new_door = stay_strategy(picked_door)
    elif strategy == "change":
        new_door = change_strategy(number_of_doors,picked_door,deleted_door)
        
    #RESULT
    if correct_door == new_door:
        correct += 1

#STATISTICS
probability = (correct/iterations)
standard_error = (math.sqrt((probability)*(1-(probability))/iterations))
sigmas = (NormalDist().inv_cdf(1-standard_error))
print("The probability to succeds is " + str(probability))
print("Standard error is " + str(standard_error))
print("The result has " + str(sigmas) + " sigmas")