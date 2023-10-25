# Exploration
#%%
# imports 
import pandas as pd
import numpy as np
from openbb_terminal.sdk import openbb
import matplotlib.pyplot as plt

#%%
snp500 = openbb.stocks.load(
    symbol='VOO'
)
# %%
snp500
# %%
# some helper functions
def prices_to_returns(data=pd.DataFrame,
                      log:bool=True,
                      col:[str]='Close')->pd.Series:
    if log:
        rets = np.log(data[col]/data[col].shift(1))
    else:
        rets = data[col].pct_change()
    return rets
#%%
log_rets = prices_to_returns(data=snp500)
# %%
log_rets

# %%
rets = prices_to_returns(data=snp500, log=False)
# %%
def realized_vol(returns)->np.array:
    return np.sqrt(np.sum(returns**2))

# %%
df = pd.DataFrame(
    {
        'close': snp500['Close'],
        'simple_return': prices_to_returns(snp500, log=False), 
        'log_return': prices_to_returns(snp500)    
    }

    
)
# %%
df
# %%
#Plot a stacked line graph
fig, ax = plt.subplots(3,1, figsize=(24,20), sharex=True)
df.close.plot(ax=ax[0])
ax[0].set(
    title="VOO Returns",
    ylabel="Stock Price ($)",
)
df.simple_return.plot(ax=ax[1])
ax[1].axhline(y=0, color='r', linestyle='-')
ax[1].set(
    xlabel="Date",
    ylabel="Simple Returns (%)"
)
df.log_return.plot(ax=ax[2])
ax[2].axhline(y=0, color='r', linestyle='-')
ax[2].set(
    xlabel='Date',
    ylabel="Log Returns (%)"
)

# %%
# Rolling calculations
def compute_rolling(data:pd.DataFrame)->np.array:
    """
    """
    pass

# %%
openbb.etf.holdings("VOO", limit=50)
# %%
