import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas

COLORS = ['b', 'g', 'r']

data = []

for filename in sys.argv[1:]:
    data.append(pandas.read_csv(filename)['Mb/s'].tolist())

plt.xlabel('seconds')
plt.ylabel('Mb/s')

for i in range(len(data)):
    plt.plot(data[i], color=COLORS[i])
plt.show()