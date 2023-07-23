import csv

def prettyPrint(d:dict):
  print("This program computes summary statistics for the Iris Dataset")
  print("-----------------------------------------------------------------------")
  word_list = d.keys()
  print("{:27s}".format("Species:"), end="")
  for w in word_list:
      print("{:15s}".format(w), end="")
  print()
  print("-----------------------------------------------------------------------")
  print("Attributes (cm): ")
  
  fields = ["Avg Petal length:","Avg Petal width:","Avg Sepal length:","Avg Sepal width:"]
    #Prints
  for i in range(4):
      print("{:18s}".format(fields[i]),end="")
      print("{:15.2f}".format(d["Setosa"][i]),end="")
      print("{:15.2f}".format(d["Versicolor"][i]),end="")
      print("{:15.2f}".format(d["Virginica"][i]),end="")
      print()

#This will calculate the average of the rows, and it will return it as a list.
def average(l:list):
  sepalLength = []
  sepalwidth = []
  petalLength = []
  petalwidth = []
  for lista in l:
      sepalLength.append(float(lista[0]))
      sepalwidth.append(float(lista[1]))
      petalLength.append(float(lista[2]))
      petalwidth.append(float(lista[3]))
  
  return [sum(petalLength)/len(petalLength), sum(petalwidth)/len(petalwidth), sum(sepalLength)/len(sepalLength), sum(sepalwidth)/len(sepalwidth)]

rows = []
#open file and reads
epa_file = open("iris.csv", "r",encoding="windows-1252")
reader = csv.reader(epa_file)
read = epa_file.readline().rstrip('\n') #skips first row 
for row in reader:
  rows.append(row)

#Lists
setosa_list = []
versicolor_list = []
virginica_list = []
#fill the list 
for row in rows:
    temp_lista = row
    if "setosa" in temp_lista:
        setosa_list.append([float(i) for i in temp_lista[:-1]])
    elif "versicolor" in temp_lista:
        versicolor_list.append([float(i) for i in temp_lista[:-1]])
    else:
        virginica_list.append([float(i) for i in temp_lista[:-1]])
      
#Create dictionary 
iris = {}
iris["Setosa"] = average(setosa_list)
iris["Versicolor"] = average(versicolor_list)
iris["Virginica"] = average(virginica_list)
#Prints
prettyPrint(iris)










