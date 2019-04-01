#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns, matplotlib.pyplot as plt
sns.set(style="whitegrid")


w = 0.8    # bar width
x = [1, 2] # x-coordinates of your bars

mu, sigma = 1, 0.5 # mean and standard deviation
norm1 = np.random.normal(mu, sigma, 50)

norm2 = np.random.normal(-1, sigma, 50)

y = [norm1, norm2]


dataset = pd.read_csv("dataset1.csv")

ax=sns.barplot(x="condition", y="score", data=dataset, capsize=.1, ci=None)
plt.ylim(350, 450)
ax.get_figure().savefig("fig1.pdf")
ax.clear()

ax=sns.barplot(x="condition", y="score", data=dataset, capsize=.1, ci=None)
ax.get_figure().savefig("fig2.pdf")
ax.clear()

ax=sns.barplot(x="condition", y="score", data=dataset, capsize=.1, ci="sd")
ax.get_figure().savefig("fig3.pdf")
ax.clear()

sns.barplot(x="condition", y="score", data=dataset, capsize=.1, ci="sd")
sns.swarmplot(x="condition", y="score", data=dataset, color="0", alpha=.5, size=20)
ax.get_figure().savefig("fig4.pdf")
ax.clear()


dataset = pd.read_csv("dataset2.csv")

sns.barplot(x="condition", y="score", data=dataset, capsize=.1, ci="sd")
sns.swarmplot(x="condition", y="score", data=dataset, color="0", alpha=.5, size=20)
ax.get_figure().savefig("dataset2-cdts.pdf")


#plt.show()

