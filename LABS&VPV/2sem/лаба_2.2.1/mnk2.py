import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('o.csv')

# lis=df['u'].tolist()
# l=[round(float(i)/42.4, 5) for i in lis]
# df1=pd.DataFrame({'dt':l})
# df['dt']=df1



x=df['1/P'].tolist()
y=df['D'].tolist()
plt.figure(figsize=(10,6))
plt.title('Эксраполяция')
plt.xlabel('1/P, Па^-1')
plt.ylabel('D')
plt.grid()
plt.errorbar(x, y, yerr=0, xerr=0, fmt='ob')
p=np.polyfit(x, y, 1)
xx=np.linspace(0, max(x), 10000)
yy=np.polyval(p, xx)
plt.plot(xx, yy, '-r', label=f'k={p[0]:.6f}, b={p[1]:.6f}')
a = 1/100191.76
b=p[0]*a+p[1]
print(b)
plt.scatter([a, a], [b, 0.00007], color='g')
plt.legend()
plt.show()
print(f'k={p[0]:.6f}')