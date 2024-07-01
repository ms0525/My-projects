import json

f = open('path/si_ti_results.json', 'r')
SI_TI = json.load(f)

import matplotlib.pyplot as plt
SI = []
TI = []
for i in SI_TI:
    print(i)
    print(SI_TI[i])
    print(SI_TI[i]['SI'])
    print(SI_TI[i]['TI'])
    print(' ')
    SI.append(SI_TI[i]['SI'])
    TI.append(SI_TI[i]['TI'])

plt.figure(figsize=(10, 6))
plt.scatter(SI, TI, color='blue')
plt.title('Scatter Plot of SI vs TI')
plt.xlabel('SI')
plt.ylabel('TI')
plt.grid(False)
plt.show()