import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_palette('Set1')

np.random.seed(1)

x1 = np.random.randint(1,613,10000) # 一様分布

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(1, 1, 1)
ax.hist(x1, bins=300, alpha=0.7)
plt.show()