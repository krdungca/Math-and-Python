#code for matrix generation ,consecutive numbers in each row and column
import numpy as np
m, n = 25, 25
a = np.arange(700, 700+m*n).reshape(m,n)
print(a)


