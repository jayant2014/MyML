import numpy as np
my_list = [1,2,3]
arr = np.array(my_list)
arr
np.arange(0,10)
np.zeros(5)
np.zeros((3,5))
np.ones(3)
np.ones((3,5))
np.linspace(0,11,100)
np.random.randint(0,10)
np.random.seed(101)
np.random.randint(0,100,10)

np.random.seed(101)
arr = np.random.randint(0,100,10)
arr
arr.max()
arr.min()
arr.mean()
arr.argmax()
arr.reshape(2,5)

mat = np.arange(0,100).reshape(10,10)
mat

mat[0,1]
mat[4,3]
mat[:,0]
mat[5,:]
mat[0:3,0:3]

my_filter = mat > 50
mat[my_filter]
mat[mat>50]


