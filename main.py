#Jonas York
#U1 L2
#Visualizing Rat

from uOneMain import *
import matplotlib.pyplot as plt

def main():
  rat_test()

  with open("bigInfo.txt",'r') as openFile:
    contents = openFile.read()
    bigContents = contents.split()

  with open("smallInfo.txt",'r') as openFile:
    contents = openFile.read()
    smallContents = contents.split()

  with open("average.txt", 'r') as openFile:
    contents = openFile.read()
    meanContents = contents.split()

  bigContents = [ int(x) for x in bigContents ]
  smallContents = [ int(x) for x in smallContents ]
  meanContents = [ int(x) for x in meanContents ]
  for dataset in [bigContents,smallContents,meanContents]:
    plt.plot(dataset)

    plt.title("Results of Rat Breeding")
    plt.xlabel("Generation Number")
    plt.ylabel("Weight in grams")
    plt.legend(["Biggest Rat","Smallest Rat","Rat Average"])
    plt.savefig("rat_graph3.png")

if __name__ == "__main__":
  main()