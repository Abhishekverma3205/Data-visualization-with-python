import matplotlib.pyplot as plt
import numpy as np
data1 = {'Roll no.':np.arange(1,51),'Marks':np.random.randint(100,size= 50)}
plt.hist(data1['Marks'],bins = 10,edgecolor= "red")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of exam Score")
plt.grid(True)
plt.show()