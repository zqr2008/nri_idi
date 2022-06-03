from nri_f import nri
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\mjdee\Desktop\nri\example.csv")
nri(df,"old_model","new_model","gold_std")