#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.rcParams['figure.figsize'] = (10.0, 5.0) # bigger figures

import pandas as pd
import seaborn as sns, matplotlib.pyplot as plt
sns.set(style="whitegrid")

dataset = pd.read_csv("dataset1.csv")


ax=sns.regplot(x="score", y="heartrate", data=dataset,label="Heart rate")
plt.savefig("dataset1-corr-heartrate.pdf")
ax.clear()

ax=sns.regplot(x="heartrate", y="score", data=dataset,label="Heart rate")
plt.savefig("dataset1-corr-score-heartrate.pdf")
ax.clear()
sns.regplot(x="score", y="age", data=dataset,label="Age")
plt.savefig("dataset1-corr-age.pdf")

#plt.show()

