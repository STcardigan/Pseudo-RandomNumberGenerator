import time
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#print(time.time(), time.clock())

a = [0 for x in range(4)]
listNum = []
while(a[0]==0 or a[3]==0):
    num = time.time()
    num = int(num)
    num = str(num)
    size = len(num)

    a[3] = num[size - 1]
    a[2] = num[size - 2]
    a[1] = num[size - 3]
    a[0] = num[size - 4]
    print(a)


a = ['6','4','8','7']
for x in range(100):

    a = [int(x)for x in a]
    #print(a)
    number = a[3] * 0.1 + a[2] * 0.01 + a[1] *0.001  + a[0]*0.0001
    listNum.append(number)
    number = a[3]*1000 + a[2]*100 + a[1]*10 + a[0]
    #print(number)
    number = number*number
    #print(number)


    tmp = [0 for x in range(len(str(number)))]
    #print(tmp)
    count = len(str(number))-1
    for i in range(1,len(str(number))+1):
        tmp[count] = number%(10)
        number = int(number/(10))
        count -= 1

    while(len(tmp)<8):
        tmp = [0] + tmp
    #print(tmp)

    a[3] = tmp[2]
    a[2] = tmp[3]
    a[1] = tmp[4]
    a[0] = tmp[5]

z = np.array(listNum)
print(z)
#pd.DataFrame(z).to_csv('middle.csv', header=False, index=False)

n, bins, patches = plt.hist(z, 50, facecolor='green')
y = mlab.normpdf( bins, 0, 1)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('random value')
plt.title(r'lib implement')

plt.grid(True)

plt.show()