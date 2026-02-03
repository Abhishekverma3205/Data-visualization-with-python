# Area Chart
import matplotlib.pyplot as plt
month=["jan",'feb','mar','apr','may','jun']
sales=[1200,1000,800,600,900,1500]
plt.figure(figsize=(6,4))
plt.plot(month,sales,marker="*")
plt.fill_between(month,sales,color="pink",alpha=0.6)
plt.show()