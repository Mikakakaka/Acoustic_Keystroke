---
title: "Acoustic Keystroke"
author: "Mikael LEGRAIN, Titouan PETIT"
---

# Acoustic Keystroke Analysis
## About The Project
***

The objective of this project is to perform biometrics using the way an individual types on the keyboard. 
It uses the pyAudioAnalysis library for most of the feature extraction and recognition of individuals. Most of the code is taken directly from the sample applications provided with the project. You can find some more information in the following article :
[Intro to Audio Analysis: Recognizing Sounds Using Machine Learning](https://hackernoon.com/intro-to-audio-analysis-recognizing-sounds-using-machine-learning-qy2r3ufl)

We have provided a small amount of data sufficient to experiment with the bases of our project. Provided with the program are present the records of 4 individuals.
In the **data/** folder are present the records necessary to constitute the classes. The 4 people have recorded here 6 times the sentence *"La biométrie est la vérification de l'identité d'un individu"*. 

The first 5 recordings allow the construction of the model while the 6th (plus a bonus, another shorter sentence) allow to check if the person is well recognized.
In the folder **to_guess/** are present the 6th recordings and the free typing of the user. 


## Installation
***
Clone this project 
```
git clone https://github.com/Mikakakaka/Acoustric_Keystroke.git
```

Before using our tool, you have to install the pyAudioAnalysis library.
```
git clone https://github.com/tyiannak/pyAudioAnalysis.git
cd pyAudioAnalysis
pip install -r ./requirements.txt
pip install -e .
```

After doing so, you are ready to go. 

## How to do
***
1. You must fill in the records in the **data/** folder with the records of the individuals you wish to enroll. Each record must be in a folder named after the desired name for the resulting class.
2. Once all the records are correctly classified, the SVN-RBF model must be trained via the train.py file. This step will take some time but should only be done once.

    ```
    python3 learn.py
    ```
3. You can see a two-dimensional representation of the features for each class in the srcipt **dots.py**.
    ```
    python3 dots.py
    ```
4. The records to be identified must be placed in the **to_guess/** folder but must not be classified in subfolders. They are therefore all in the root of the folder. 
5. Once the training is done and the files are correctly classified, you can classify all the recordmlents via the **biometry.py** script.
    ```
    python3 biometry.py
    ``` 
6. The script **authentication.py** is the beginning of the authentication protocol. The final idea is to integrate a real time sound recording but for the moment, this program takes the main lines of the **biometry.py** script but asks the user to enter his name. The program will then retrieve all the records and models in which it is present. If the individual is indeed the one recognized by the program, then his authentication is granted. At the moment, this program simply allows to focus on a single individual and to visualize the same information as the first tool but removing all the extra information. 
    ```
    python3 authentication.py
    ``` 

## Some More Info
***
* As you can see in the article quoted above, some parameters can be modified like the length of the frames or the steps. In our case, referring to the different information provided by the pyAudioAnalysis library, it corresponds to the parameters *m_win, m_step, s_win, s_step* in **dots.py** or *mt, st* in **learn.py**. Those values are in seconds.
* You can change the type of learning. By default, SVM-RBF is used but pyAudioAnalysis allows to use KNN, SVM or RandomTrees among others. We have tested with SVM-RBF, KNN and SVM but we are not sure about the compatibility with the others. 
  
    To make the change, you just have to modify the parameter **"svm-rbf "** in *extract_features_and_train()* of the file **learn.py** or *file_classification()* in **authentication.py** and **biometry.py** depending on the desired strategy. Of course, it is also necessary to modify the nomenclature of the files that use them.


## Errors you can encounter
***
You might need to deal with the following errors.

* Tkinter not found on linux :
    ```
    sudo apt-get install python3-tk
    ```

* You can encounter some warning about unpickling estimator SVC from certain versions using the regognotion scripts.
    ```
    pip install -U scikit-learn
    ```