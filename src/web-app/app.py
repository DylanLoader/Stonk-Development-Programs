#%% Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pyfolio as pf

#%% Main
st.title('Portfolio Analysis')

# Global Vars
DATA_PATH = Path("data/")
SNP_FILE = DATA_PATH / "snp500/snp500.csv"
PORTFOLIO_FILE = DATA_PATH / "portfolio/aapl.csv"

#%% Data

# We use @st.cache_data to keep the dataset in cache
# @st.cache_data
def get_data():
    snp500 = pd.read_csv(SNP_FILE)
    portfolio = pd.read_csv(PORTFOLIO_FILE)
    return snp500, portfolio


snp500, portfolio = get_data()

# %%
# chart_data = pd.DataFrame({"SNP500": snp500[["date","Close"]], "Portfolio":portfolio[["date", "Close"]]}) 
st.subheader('VOO Return Table')

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
# # joined_df = snp500[["date", "Close"]].merge(portfolio[["date", "Close"]], 
# #                                             on="date",
# #                                             suffixes=("_snp500", "_portfolio"))
# # #%%
# # returns_df = compute_returns(joined_df, col=['Close_snp500', 'Close_portfolio'], log=False, keep_date=True)
# # compute_returns(joined_df, col=['Close_snp500', 'Close_portfolio'])
# cumulative_returns_df = returns_df.cumsum()

#%%
# cumulative_returns_df.head()


#%%
# st.line_chart(cumulative_returns_df, x=None, y=['Close_snp500', 'Close_portfolio'])

#%%
# joined_df

# %%
# pf.create_returns_tear_sheet(joined_df.iloc[:,1])

#%%
# joined_df.loc[:,1]
# %%
import yfinance as yf
voo = yf.Ticker('VOO')
history = voo.history('max')
# history.index = history.index.tz_convert('utc')
#%%
history

#%%
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Generate candlestick plot with volume
# fig=make_subplots(
#     # 
#     rows=2, 
#     cols=1, 
#     shared_xaxes=True,
#     vertical_spacing=0.05, 
#     subplot_titles=("Candle Stick", "Volume"), row_width=[0.3, 0.6]
#     )
st.subheader('VOO OHLC Candlestick Plot')
from plotly.subplots import make_subplots
fig = make_subplots(rows = 2, 
                    cols = 1,
                    shared_xaxes = True,
                    vertical_spacing = 0.03,
                    row_heights= [0.75, 0.25])

fig.add_trace(
    go.Candlestick(x=history.index,
    open=history['Open'],
    high=history['High'],
    low=history['Low'],
    close=history['Close'], name="OHLC")
    )
fig.add_trace(
    go.Bar(x=history.index, 
           y=history['Volume'], 
           name="Volume"),row=2,col=1
    )
# Add y axis titles
fig.update_yaxes(
    title_text = "Price", row = 1, col = 1
    )
 
fig.update_yaxes(
    title_text = "Volume", row = 2, col = 1
    )

fig.update_layout(
    xaxis_rangeslider_visible = False,
    showlegend = False
    )
st.plotly_chart(fig)

# gen_candle(history)
#%%
# history
#%%
# returns = history['Close'].pct_change()

#%%
# pf.create_returns_tear_sheet(returns, live_start_date='2020-1-1')
#%%
