#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns, matplotlib.pyplot as plt
sns.set(style="whitegrid")


anscombe = pd.read_csv("anscombe.csv")
I = anscombe[anscombe["quartet"] == "I"]
II = anscombe[anscombe["quartet"] == "II"]
III = anscombe[anscombe["quartet"] == "III"]
IV = anscombe[anscombe["quartet"] == "IV"]

f, axes = plt.subplots(2, 2, sharex=True, sharey=True)
sns.regplot(I.x, I.y,ax=axes[0][0], ci=None)
sns.regplot(II.x, II.y,ax=axes[0][1], ci=None)
sns.regplot(III.x, III.y,ax=axes[1][0], ci=None)
sns.regplot(IV.x, IV.y,ax=axes[1][1], ci=None)
plt.savefig("anscombe.pdf")
#plt.show()

