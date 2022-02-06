from pyAudioAnalysis.audioTrainTest import extract_features_and_train
from itertools import combinations
from time import perf_counter
from glob import *
import os.path

mt, st = 1.0, 0.05

dirs=glob("data"+os.sep+"*")

if ".DS_Store" in dirs :
	dirs.remove(".DS_Store")

combinations_list=[]
for i in combinations(dirs,2):
    print([i[0].split(os.sep)[1],i[1].split(os.sep)[1]])
    combinations_list.append(i)

print("Number of combinaisons : ",len(combinations_list))

for couple in combinations_list :
    tic=perf_counter()
    svm_file_name="trained_data_svm_rbf"+os.sep+"svm_rbf"+couple[0].split(os.sep)[1]+"_"+couple[1].split(os.sep)[1]
    extract_features_and_train(couple, mt, mt, st, st, "svm_rbf", svm_file_name)
    tac=perf_counter()
    print("Analyse time : ",tac-tic)