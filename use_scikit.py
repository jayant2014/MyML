from numpy as np
from sklearn.preprocessing import MinMaxScaler
data = np.random.randint(0,100,(10,2)
data
scaler_model = MinMaxScaler()
scaler_model.fit(data)
scaler_model.transform(data)
scaler_model.fit_transform(data)

import pandas as pd
mydata = np.random.randint(0,101,(50,4))
mydata
df = pd.DataFrame(data=mydata, columns = ['f1', 'f2', 'f3', 'label'])
df
x = df[['f1', 'f2', 'f3']]
y = df['label']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.33, random_state = 42)
x_train.shape
x_test.shape
