import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def get_random(seed_1, seed_2, seed_3):
  
    seed_1 = 171 * (seed_1 % 177) - 2*(seed_1 / 177)
    if seed_1 < 0:
        seed_1 += 30269
      
    seed_2 = 172 * (seed_2 % 176) - 35*(seed_2 / 176)
    if seed_2 < 0:
        seed_2 += 30307
         
    seed_3 = 170 * (seed_3 % 178) - 63*(seed_3 / 178)
    if seed_2 < 0:
        seed_2 += 30323
     
    temp = seed_1 / 30269 + seed_2/30307 + seed_3/30323
    return temp - int(temp),seed_1,seed_2,seed_3

s1 = 3456
s2 = 2897
s3 = 6980
listVal = []

for i in range(10000000):
    val,s1,s2,s3 = get_random(s1,s2,s3)
    listVal.append(val)


listVal = [ round(elem, 3) for elem in listVal ]
listVal = [ abs(elem) for elem in listVal ]
z = np.array(listVal)
print(z)
#pd.DataFrame(z).to_csv('wich.csv', mode='w', header=False, index=False)

n, bins, patches = plt.hist(z, 50, facecolor='green')
y = mlab.normpdf( bins, 0, 1)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('random value')
plt.title(r'lib implement')

plt.grid(True)

plt.show()