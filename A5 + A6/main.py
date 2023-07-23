import csv
import numpy

def prettyPrint(d:dict):
  print("This program computes summary statistics for the Iris Dataset")
  print("--------------------------------------------------------------------------------")
  print("{:27s}".format("Species: Setosa"), end="")
  print("{:15s}".format("Average"), end="")
  print("{:15s}".format("Max"), end="")
  print("{:15s}".format("Min"), end="")
  print("{:15s}".format("Std"), end="")
  print("Count: ",len(setosa_list))
  print("--------------------------------------------------------------------------------")
  print("Attributes (cm): ")
  
  fields = ["Petal length:","Petal width:","Sepal length:","Sepal width:"]
    #Prints
  for i in range(4):
      print("{:18s}".format(fields[i]),end="")
      print("{:15.2f}".format(d["Setosa_average"][i]),end="")
      print("{:15.2f}".format(d["Setosa_max"][i]),end="")
      print("{:15.2f}".format(d["Setosa_min"][i]),end="")
      print("{:15.2f}".format(d["Setosa_std"][i]),end="")
      print()
  print("--------------------------------------------------------------------------------")
  print("{:27s}".format("Species: Versicolor"), end="")
  print("{:15s}".format("Average"), end="")
  print("{:15s}".format("Max"), end="")
  print("{:15s}".format("Min"), end="")
  print("{:15s}".format("Std"), end="")
  print("Count: ",len(versicolor_list))
  print("--------------------------------------------------------------------------------")
  print("Attributes (cm): ")
  
  fields = ["Petal length:","Petal width:","Sepal length:","Sepal width:"]
    #Prints
  for i in range(4):
      print("{:18s}".format(fields[i]),end="")
      print("{:15.2f}".format(d["Versicolor_average"][i]),end="")
      print("{:15.2f}".format(d["Versicolor_max"][i]),end="")
      print("{:15.2f}".format(d["Versicolor_min"][i]),end="")
      print("{:15.2f}".format(d["Versicolor_std"][i]),end="")
      print()
  print("--------------------------------------------------------------------------------")
  print("{:27s}".format("Species: Virginica"), end="")
  print("{:15s}".format("Average"), end="")
  print("{:15s}".format("Max"), end="")
  print("{:15s}".format("Min"), end="")
  print("{:15s}".format("Std"), end="")    
  print("Count: ",len(virginica_list))
  print("--------------------------------------------------------------------------------")
  print("Attributes (cm): ")
  
  fields = ["Petal length:","Petal width:","Sepal length:","Sepal width:"]
    #Prints
  for i in range(4):
      print("{:18s}".format(fields[i]),end="")
      print("{:15.2f}".format(d["Virginica_average"][i]),end="")
      print("{:15.2f}".format(d["Virginica_max"][i]),end="")
      print("{:15.2f}".format(d["Virginica_min"][i]),end="")
      print("{:15.2f}".format(d["Virginica_std"][i]),end="")
      print()
  print("--------------------------------------------------------------------------------")
  print("{:27s}".format("Species: All"), end="")
  print("{:15s}".format("Average"), end="")
  print("{:15s}".format("Max"), end="")
  print("{:15s}".format("Min"), end="")
  print("{:15s}".format("Std"), end="")    
  print("Count: ",len(rows))
  print("--------------------------------------------------------------------------------")
  print("Attributes (cm): ")
  
  fields = ["Petal length:","Petal width:","Sepal length:","Sepal width:"]
    #Prints
  for i in range(4):
      print("{:18s}".format(fields[i]),end="")
      print("{:15.2f}".format(d["row_average"][i]),end="")
      print("{:15.2f}".format(d["row_max"][i]),end="")
      print("{:15.2f}".format(d["row_min"][i]),end="")
      print("{:15.2f}".format(d["row_std"][i]),end="")
      print()


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


def mini(l:list):
  sepalLength = []
  sepalwidth = []
  petalLength = []
  petalwidth = []
  for lista in l:
      sepalLength.append(float(lista[0]))
      sepalwidth.append(float(lista[1]))
      petalLength.append(float(lista[2]))
      petalwidth.append(float(lista[3]))
  
  return [ min(petalLength),min(petalwidth), min(sepalLength), min(sepalwidth)] 


def maxi(l:list):
  sepalLength = []
  sepalwidth = []
  petalLength = []
  petalwidth = []
  for lista in l:
      sepalLength.append(float(lista[0]))
      sepalwidth.append(float(lista[1]))
      petalLength.append(float(lista[2]))
      petalwidth.append(float(lista[3]))
  
  return [ max(petalLength),max(petalwidth), max(sepalLength), max(sepalwidth) ] 


def std(l:list):
  sepalLength = []
  sepalwidth = []
  petalLength = []
  petalwidth = []
  for lista in l:
      sepalLength.append(float(lista[0]))
      sepalwidth.append(float(lista[1]))
      petalLength.append(float(lista[2]))
      petalwidth.append(float(lista[3]))
  
  return [numpy.std(petalLength), numpy.std(petalwidth), numpy.std(sepalLength), numpy.std(sepalwidth)] 

 
rows = []
#open file and reads (skips first row)
epa_file = open("iris.csv", "r",encoding="windows-1252")
reader = csv.reader(epa_file)
read = epa_file.readline().rstrip('\n') 

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
iris["Setosa_average"] = average(setosa_list)
iris["Versicolor_average"] = average(versicolor_list)
iris["Virginica_average"] = average(virginica_list)
iris["row_average"] = average(rows)

iris["Setosa_max"] = maxi(setosa_list)
iris["Versicolor_max"] = maxi(versicolor_list)
iris["Virginica_max"] = maxi(virginica_list)
iris["row_max"] = maxi(rows)

iris["Setosa_min"] = mini(setosa_list)
iris["Versicolor_min"] = mini(versicolor_list)
iris["Virginica_min"] = mini(virginica_list)
iris["row_min"] = mini(rows)

iris["Setosa_std"] = std(setosa_list)
iris["Versicolor_std"] = std(versicolor_list)
iris["Virginica_std"] = std(virginica_list)
iris["row_std"] = std(rows)

#Prints
prettyPrint(iris)
