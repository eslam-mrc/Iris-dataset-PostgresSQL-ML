import numpy as np
import pandas as pd
import pickle
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sqlalchemy as db
import sys
import psycopg2
import time

# create connection with the database
con = db.create_engine('postgresql://iti:iti@localhost/data_mgmt')

# getting the id of the row that was just inserted
query1 = """
SELECT MAX(id)
FROM flower_dim
"""
time.sleep(5)
maxID = con.execute(query1).fetchone()[0]
print(maxID)

# selecting the row that was just inserted to extract the values
query2 = """
SELECT *
FROM flower_dim
WHERE id = %s
"""
row = con.execute(query2, (maxID)).fetchone()
sepalLength = row[1]
sepalWidth = row[2]
petalLength = row[3]
petalWidth = row[4]

# calling model to predict the type of the flower
filename = '/home/eslam/Downloads/Task5/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
pred = loaded_model.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])[0]


# inserting the values and the prediction in a new table
query3 = """
INSERT INTO flower_type
VALUES (%s, %s, %s, %s, %s)
"""
con.execute(query3, (sepalLength, sepalWidth, petalLength, petalWidth, pred))

