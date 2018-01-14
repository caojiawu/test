
# coding: utf-8

# In[63]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sklearn.covariance as cor

os.chdir('d:\\testcode')
data = pd.read_csv('train.csv')

c = np.zeros(100)

for i in range(100):
    c[i]=i+np.random.randint(50)


plt.plot(c,'.b',range(100)+25*np.ones(100),'r')
plt.show()



# In[47]:


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
plt.figure();ts.plot();plt.show()
ts1 = ts.cumsum()
plt.figure();ts1.plot();plt.show()


# In[90]:


np.shape(data[data['Cabin'].notnull()])
data[data['Cabin'].notnull()].groupby('Cabin').first()


# In[122]:


#data['Pclass'].corr(data['Survived'])
data.dtypes

