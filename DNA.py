
import random
import string 



#! CONVERT genes into LIST otherwise mating won't work.

# representation of an individual in the population : DNA
class DNA: 
    # length of the genes : genelength
    genelength=19
    mutationrate=0.01

    def __init__(self): 
        self.genes = [chr(random.randint(32,128)) for x in range(self.genelength)]
        self.fitnessScore = float(0) 

# no. of correct characters in our DNA from the target string.
    def fitness(self,targetstr):
        score=0
        for x in range(len(targetstr)):
            if targetstr[x] == self.genes[x]:
                score = score + 1
        fitness = score/len(targetstr)
        # print("fitness: {} \n".format(fitness))
        self.fitnessScore = fitness
        # print("fitness: {}".format(self.fitnessScore))                
        return fitness

    def crossover(self, partner): 
        child = DNA() 
        midpoint = random.randint(0,self.genelength)

        for x in range(self.genelength):
            if x > midpoint : 
                child.genes[x] = self.genes[x]
            else: 
                child.genes[x] = partner.genes[x]
        
        return child
                
    def mutate(self): 
        for x in range(self.genelength):
            if random.random() < self.mutationrate : 
                self.genes[x] = chr(random.randint(32,128))

    def show(self): 
        text = ''.join(str(letter) for letter in self.genes)
        # print(text)
        return text 

