from nri_f import nri
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\mjdee\Desktop\nri\tablefor_NRI.csv")
df_output = nri(df,"saps_pro","xgboost","alive")
df_output.to_csv(r"C:\Users\mjdee\Desktop\nri\result_NRI.csv")
