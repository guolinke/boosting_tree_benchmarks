import pandas as pd
import numpy as np
from sklearn.datasets import dump_svmlight_file
from sklearn.preprocessing import LabelEncoder

# generate one-hot data
d = pd.read_csv("all.csv")
X = d.drop('dep_delayed_15min', 1)
y = d[["dep_delayed_15min"]]
X_1hot = pd.get_dummies(X).to_sparse()
y_num = np.where(y=="Y",1,0)[:,0]
dump_svmlight_file(X_1hot.values[:10000000,:], y_num[:10000000], 'dataexpo_onehot.train')
dump_svmlight_file(X_1hot.values[10000000:,:], y_num[10000000:], 'dataexpo_onehot.test') 

# generate data with categorical feature
categorical_names = ["Month" , "DayofMonth" , "DayOfWeek" , "UniqueCarrier" , "Origin" , "Dest" ]
for name in categorical_names:
    le = LabelEncoder().fit(X[name])
    X[name]  = le.transform(X[name])

dump_svmlight_file(X.values[:10000000,:], y_num[:10000000], 'dataexpo.train')
dump_svmlight_file(X.values[10000000:,:], y_num[10000000:], 'dataexpo.test') 
