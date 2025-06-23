import numpy as np
arr = np.array(range(1,101,1))

even = [int(x) for x in arr if x %2 == 0]
print(even)