import numpy as np
# li=[1,2,3,4,5,6,7,8,9]
# print(type(li))
# ar=np.array([1,2,3,4,5])
# print(type(ar))
#
# li=[1,2,3,4,5,6,7,8,9]
# arr=np.array(li)
# print(arr/2)
# arr=np.array(range(18))
# arr=arr.reshape((3,6))
# print(arr)

#csv file is comma separated values

import pandas as pd
sr=pd.Series(['1','2','3'])
print(sr)

userData={'name':['Sheheryar','Ali','Subhani'],'age':[21,23,20]}
df=pd.DataFrame(userData)
print(df)