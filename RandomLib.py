import random
import numpy as np
import matplotlib.mlab as mlab

from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
#for i in range(10**11):
    #print(random.random())

x = list()
for i in range(1):
    x = []
    for j in range(300):
        x.append(random.random())
    z = np.array(x)
    pd.DataFrame(z).to_csv('normal.csv', mode='w', header=False, index=False)
    print(i)

counts = Counter(z)
labels, values = zip(*counts.items())
# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.1

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()