from ast import increment_lineno
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
#Importring data plotting libraaries
from matplotlib import pyplot as plt

dataset = load_digits()

#Dictionary of keys
key=dataset.keys()
print(key)
#Array of pixels
data=dataset.data[0]
print(data)
#Reshaping one dimensional array into two dimentional array
reshaped_data=dataset.data[39].reshape(8,8)
print(reshaped_data)


# gray image
plt.gray
#Showing metric
plt.matshow(reshaped_data)
#showing plots
plt.show()