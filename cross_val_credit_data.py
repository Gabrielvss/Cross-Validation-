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
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
 
#training and results
classificador = GaussianNB()
resultado = cross_val_score(classificador, previsores, classe, cv = 10) 
resultado.mean()
resultado.std()
