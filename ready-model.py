import numpy as np
import pandas as pd
import pickle
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('../path/to/dataset/iris.csv')

X = data.drop(['species'], axis=1)
y = data['species']


#Splitting data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)

knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

# save the model to disk
filename = '/path/to/model/finalized_model.sav'
pickle.dump(knn, open(filename, 'wb'))

