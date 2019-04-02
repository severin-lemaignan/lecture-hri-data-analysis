#! /usr/bin/env python3

import numpy as np

import pandas as pd
import seaborn as sns, matplotlib.pyplot as plt
sns.set(style="whitegrid")

mu, sigma = 1, 0.5 # mean and standard deviation
norm1 = np.random.normal(mu, sigma, 100)
#sns.distplot(norm1)

norm2 = np.random.normal(-mu, sigma, 100)
#sns.distplot(norm2)

means = (1, 2)
#bimodal = np.random.binomial(means, cov, 100)

#sns.distplot(bimodal)

dataset = pd.read_csv("dataset1.csv")

sns.distplot(dataset[dataset["condition"]=="control"]["score"], bins=10)
plt.savefig("distributions-control.pdf")
ax=sns.distplot(dataset[dataset["condition"]=="cdt1"]["score"], bins=10)
plt.savefig("distributions.pdf")

ax.clear()

dataset = pd.read_csv("dataset2.csv")
sns.distplot(dataset[dataset["condition"]=="control"]["score"], bins=10)
sns.distplot(dataset[dataset["condition"]=="cdt1"]["score"], bins=10)
plt.savefig("distributions2.pdf")

ax.clear()

dataset = pd.read_csv("dataset3.csv")
sns.distplot(dataset[dataset["condition"]=="control"]["score"], bins=10)
sns.distplot(dataset[dataset["condition"]=="cdt1"]["score"], bins=10)
plt.savefig("distributions3.pdf")


