import numpy as  np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv("Blood Transfution.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values
from sklearn.model_selection import train_test_split