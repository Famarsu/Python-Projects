import random
random.seed()

#INPUTS
number_of_doors=int(input("number of doors "))
iterations=int(input("iterations "))
correct = 0

#PLAY
for i in range(1,iterations+1):
    #SET-UP
    correct_door = (random.randint(1,number_of_doors))
    picked_door = (random.randint(1,number_of_doors))
    deleted_door = (random.randint(1,number_of_doors))
    while deleted_door == correct_door or deleted_door == picked_door:
        deleted_door = (random.randint(1,number_of_doors))

    #STAY STRATEGY
    """comment the CHANGE STRATEGY"""
    new_door = picked_door

    #CHANGE STRATEGY
    new_door = (random.randint(1,number_of_doors))
    while new_door == picked_door or new_door == deleted_door:
        new_door = (random.randint(1,number_of_doors))
        
    #OUTPUT
    """ print("Deleted door was n: " + str(deleted_door))
    print("Picked_door was n: " + str(picked_door))
    print("Correct door was n: " + str(correct_door)) """
    if correct_door == new_door:
        correct += 1
"""         print("YAAAY")
    else:
        print("NAAAY") """

#STATISTICS
print("The strategy succeds in a " + str(100*correct/iterations) + "% of the cases")