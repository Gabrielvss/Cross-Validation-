#preprocessing for data base
import pandas as pd

base = pd.read_csv('credit-data.csv')
base.loc[base.age < 0, 'age'] = 40.92
               
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#import the function
from sklearn.naive_bayes import GaussianNB


import numpy as np

b= np.zeros(shape=(previsores.shape[0], 1))

#import cross validation with stratifiedkfold
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
kfold = StratifiedKFold(n_splits = 10, shuffle = True, random_state = 0)
resultados = []

for indice_treinamento, indice_teste in kfold.split(previsores,
                                                    np.zeros(shape=(previsores.shape[0], 1))):
    #look how to the function StratifiedKfold work 
    #print('indice treinamento:', indice_treinamento, 'indice_teste: ', indice_teste)
    
    #training and results
    classificador = GaussianNB()
    classificador.fit(previsores[indice_treinamento],classe[indice_treinamento])
    previsoes = classificador.predict(previsores[indice_teste])
    precisao = accuracy_score(classe[indice_teste], previsoes)
    resultados.append(precisao)

#mean of results of each splits
resultados = np.asarray(resultados)
resultados.mean()


