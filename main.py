#Jonas York
#U1 L1
#Breeding rats 

# Im am very cheesed to do this lab

from rats import Rat
import random
import time

GOAL = 50000                # Target average weight (grams)
NUM_RATS = 20               # Max adult rats in the lab
INITIAL_MIN_WT = 200        # The smallest rat (grams)
INITIAL_MAX_WT = 600        # The chonkiest rat (grams)
INITIAL_MODE_WT = 300       # The most common weight (grams)
MUTATE_ODDS = 0.01          # Liklihood of a mutation
MUTATE_MIN = 0.5            # Scalar mutation - least beneficial
MUTATE_MAX = 1.2            # Scalar mutation - most beneficial
LITTER_SIZE = 8             # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10   # How many generations are created each year
GENERATION_LIMIT = 500      # Generational cutoff - stop breeded no matter what

def initial_population():
  '''Create the initial set of rats based on constants'''
  rats = [[],[]]
  mother = Rat("F", INITIAL_MIN_WT)
  father = Rat("M", INITIAL_MAX_WT)
  
  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1
  
    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)
  return rats

def calculate_weight(sex, mother, father):
  '''Generate the weight of a single rat'''
  
  
  # Use the triangular function from the random library to skew the 
  #baby's weight based on its sex
  min = mother.getWeight()
  max = father.getWeight()

  if sex == "M":
    wt = int(random.triangular(min, max, max))
  else:
    wt = int(random.triangular(min, max, min))

  return wt

def mutate(pups):
  """Check for mutability, modify weight of affected pups"""
  for gender in pups:
    for rat in gender:
      if random.random() <= MUTATE_ODDS:
        rat.weight = rat.weight*random.uniform(MUTATE_MIN,MUTATE_MAX)
        rat.weight = round(rat.weight)
      

  return pups  

def breed(rats):
  """Create mating pairs, create LITTER_SIZE children per pair"""

  children=[[],[]]
  random.shuffle(rats[0])
  random.shuffle(rats[1])

  for mate, father in enumerate(rats[0]):
    mother = rats[1][mate]
    for r in range(LITTER_SIZE):
      sex = random.choice(["M","F"])
      if sex == "M":
        ind = 0
      else:
        ind = 1 
      
      father.litters += 1
      mother.litters += 1 
      wt = calculate_weight(sex,mother,father)
      P = Rat(sex,wt)
      children[ind].append(P)

  return children  

def select(rats, pups):
  '''Choose the largest viable rats for the next round of breeding'''
  for pup in pups[0]:
    if pup.canBreed():
      rats[0].append(pup)
  for pup in pups[1]:
    if pup.canBreed():
      rats[1].append(pup)
  
  rats[0].sort()
  rats[1].sort()

  rats[0] = rats[0][-10:]
  rats[1] = rats[1][-10:]

  bigMale = rats[0][-1]
  bigFemale = rats[1][-1]

  if bigMale > bigFemale: 
    largest = bigMale
  elif bigMale < bigFemale:
    largest = bigFemale
  else:
    largest = bigMale


  return rats, largest

def calculate_mean(rats):
  '''Calculate the mean weight of a population'''
  sumWt = 0
  numRats = 0
  for rat in rats[0]:
    sumWt += rat.getWeight()
    numRats += 1
  for rat in rats[1]:
    sumWt += rat.getWeight()
    numRats += 1
  

  return sumWt // numRats

def fitness(rats):
  """Determine if the target average matches the current population's average"""
  mean = calculate_mean(rats)
  
  return mean >= GOAL, mean

def main():
  startTime = time.time()
  rats = initial_population()
  goalStatus = False
  pups = [[],[]]
  listMeans = []
  generations = 1
  while goalStatus == False:
    goalStatus, mean = fitness(rats)
    rats, largest = select(rats,pups)
    pups = breed(rats)
    pups = mutate(pups)
    listMeans.append(mean)
    generations += 1

  endTime = time.time()
  years = generations // 10
  finishTime = round(endTime - startTime, 4)

  print((" RESULTS ").center(30,"~"))
  print(f"\n\nFinal Population Mean: {mean} grams\n\n")
  print(f"Generations: {generations}")
  print(f"Experiment Duration: ~{years} years")
  print(f"Simulation Duration: {finishTime} seconds\n\n")
  print("✨ LARGEST RAT ✨")
  print(f"🐀 ({largest.getSex()})- {largest.getWeight()}g\n\n")
  print("\nGeneration Weight Average (grams)\n")
  for i, m in enumerate(listMeans):
    print(f"{m}", end="\t")
    if (i + 1) % 10 == 0:
      print("")
if __name__ == "__main__":
  main()