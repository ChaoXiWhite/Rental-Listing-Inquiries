import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()

train_df = pd.read_json('train.json')
train_df.head()