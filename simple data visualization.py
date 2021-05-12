#import the library first, remember use jupyter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#open up the csv files
weather = pd.read_csv("test.csv")
weather

#make the graph
weather.plot(x="Month", y="Sun")