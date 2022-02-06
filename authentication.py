# Example7: use trained model from Example6 
# to classify an unknown sample (song)
from importlib.metadata import files
from pyAudioAnalysis import audioTrainTest as aT
from itertools import combinations
from statistics import *
from glob import *
import os.path

files_of_models=glob("trained_data_svm_rbf"+os.sep+"*")
dirs=glob("data"+os.sep+"*")

individual=input("\n\nEnter your name : ")
print("\n")

files_to_test_global=glob("to_guess"+os.sep+"*")
files_to_test=[]
for file in files_to_test_global :
	if individual in file :
		files_to_test.append(file)

combinations_list=[]
for i in combinations(dirs,2):
	if individual in i[0] or individual in i[1]:
		print(i)
		combinations_list.append(i)

print("Number of combinaisons : ",len(combinations_list))

dico={}
for f in files_to_test:
	if individual in f :
		dico[f.split(os.sep)[1]]={}


for couple in combinations_list :
	name_1=couple[0].split(os.sep)[1]
	name_2=couple[1].split(os.sep)[1]

	for file in files_of_models :
		if name_1 in file and name_2 in file and "MEANS" not in file:
			svm_file_name=file

	for f in files_to_test:
		file_name=f.split(os.sep)[1]
		#c, p, p_nam = aT.file_classification(f, svm_file_name,"svm")
		#c, p, p_nam = aT.file_classification(f, svm_file_name,"knn")
		c, p, p_nam = aT.file_classification(f, svm_file_name,"svm_rbf")
		if name_1 not in dico[file_name]:
			dico[file_name][name_1]=[]
		if name_2 not in dico[file_name]:
			dico[file_name][name_2]=[]
		dico[file_name][name_1].append(p[0])
		dico[file_name][name_2].append(p[1])

		#print(f'P({p_nam[0]}={p[0]})')
		#print(f'P({p_nam[1]}={p[1]})')
		#print()


for key in dico :
	liste_of_percent=["",0]
	print(key)
	for value in dico[key]:
		mean_value=mean(dico[key][value]).round(3)
		print(value,":",mean_value)
		if mean_value>liste_of_percent[1]:
			liste_of_percent=(value,mean_value)
	print(key, "correspond to",liste_of_percent[0],"with an assurance of",liste_of_percent[1])
	print()
	if individual == liste_of_percent[0] :
		print("Welcome", individual, liste_of_percent[1])
	else : 
		print("You're not allowed", liste_of_percent[1])
	print()
