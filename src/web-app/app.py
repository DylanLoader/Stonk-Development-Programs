#%% Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#%% Main
st.title('Portfolio Analysis')

# Global Vars
DATA_PATH = Path("./data/")
SNP_FILE = DATA_PATH / "snp500/snp500.csv"
PORTFOLIO_FILE = DATA_PATH / "portfolio/aapl.csv"

#%% Data

# We use @st.cache_data to keep the dataset in cache
@st.cache_data
def get_data():
    snp500 = pd.read_csv(SNP_FILE)
    portfolio = pd.read_csv(PORTFOLIO_FILE)
    return snp500, portfolio


snp500, portfolio = get_data() 

# %%
# chart_data = pd.DataFrame({"SNP500": snp500[["date","Close"]], "Portfolio":portfolio[["date", "Close"]]}) 
st.subheader('Cumulative Returns Comparison')

def compute_returns(data=pd.DataFrame,
                      log:bool=True,
                      col:[str]='Close',
                      keep_date:bool=False)->pd.Series:
    if log:
        rets = np.log(data[col]/data[col].shift(1))
    else:
        rets = data[col].pct_change()
    if keep_date:
        rets = rets.set_index(data['date'])
        
    return rets



#%%
joined_df = snp500[["date", "Close"]].merge(portfolio[["date", "Close"]], 
                                            on="date",
                                            suffixes=("_snp500", "_portfolio"))
#%%
returns_df = compute_returns(joined_df, col=['Close_snp500', 'Close_portfolio'], log=False, keep_date=True)
# compute_returns(joined_df, col=['Close_snp500', 'Close_portfolio'])
cumulative_returns_df = returns_df.cumsum()

#%%
cumulative_returns_df.head()


#%%
st.line_chart(cumulative_returns_df, x=None, y=['Close_snp500', 'Close_portfolio'])

# %%
