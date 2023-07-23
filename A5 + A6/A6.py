import csv
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

print(len(rows))  
#Create dictionary 
iris = {}
iris["Setosa"] = average(setosa_list)
iris["Versicolor"] = average(versicolor_list)
iris["Virginica"] = average(virginica_list)
#Prints
#prettyPrint(iris)







