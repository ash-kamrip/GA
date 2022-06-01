
from DNA import DNA 
import random

totalMembers=150
targetstr='to be or not to be.'
found = False

def normalize(lst): 
    newlst = []
    each_mini = 101
    each_max = -1 
    for each in lst: 
        if each > each_max: 
            each_max = each 
        if each < each_mini: 
            each_mini = each 
    for each in lst: 
        each = each - each_mini
        each = each/(each_max - each_mini)
        newlst.append(round(each,2))
    return newlst

# creation of mating pool 
#-------------------------------
# each n determines the no. of a particular individual in the pool , hence creating a random 
# distribution of the mating pool, giving a chance even to individual with less fitness.
def naturalSelection(population,targetstr):
    matingpool = []
    fitnesslst=[]
    # calculating and storing the fitnessScore
    for x in population:
        fitnesslst.append(x.fitness(targetstr))
    
    fitnesslst = normalize(fitnesslst)

    for x in range(totalMembers): 
        for y in range(int(fitnesslst[x]*100)): 
            matingpool.append(population[x])
    return matingpool

if __name__=='__main__': 

    # step 1 : population generated
    population = [ DNA() for x in range(totalMembers) ]


    # generation loop
    gen = 0 
    while True: 
        # mating
        # step 2 : creating a mating pool
        matingpool = naturalSelection(population,targetstr) 

        for x in range(totalMembers):
            # step 3 : Reproduction
            parent1 = random.choice(matingpool)
            parent2 = random.choice(matingpool)
            child = parent1.crossover(parent2)
            child.mutate()

            # replacing old individual with the new individual
            # basically creating a whole new gen
            population[x] = child
            #
            child.fitness(targetstr)

        # finding the best individual in every gen
        bestone = float(0)
        bestindividual = DNA() # temp individual
        for y in population: 
            # print("fitness: {}".format(y.fitnessScore))
            if y.fitnessScore > bestone :
                bestone = y.fitnessScore
                bestindividual = y
        if gen%10 == 0 : 
            print("Generation : {} \n".format(gen))
            print("Fitness percentage : {:.2f}%".format(bestone*100))
            print("fittest individual : {} \n".format(bestindividual.show()))
            if bestone == 1: 
                break 
        gen = gen + 1 
                
        








    

