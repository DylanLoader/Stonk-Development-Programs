#%%
# imports 
import pandas as pd
import numpy as np
from openbb_terminal.sdk import openbb
import matplotlib.pyplot as plt
# %%
snp500 = openbb.stocks.load(
    symbol='VOO', 
    start_date="2000-11-13",
)

# %%
snp500.to_csv('../snp500.csv')

# %%
aapl = openbb.stocks.load(
    symbol='AAPL',
    start_date="2000-11-13")
# %%
aapl.to_csv('../aapl.csv')
# %%
