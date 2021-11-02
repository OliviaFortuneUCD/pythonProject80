import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
tips = sns.load_dataset("tips")
df = tips.copy()
sns.set(style="darkgrid")
#sns.relplot(x = "total_bill", y = "tip", hue = "smoker", col = "time", data = df);
#sns.relplot(x = "total_bill", y = "tip", hue = "smoker", col = "day", data = df);
sns.countplot(x = "day", hue = "size", palette = "ch:.25", data = df);
