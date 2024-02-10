# %%
import pandas as pd

df = pd.read_csv('BTC_USD_2013-10-01_2020-03-26-CoinDesk.csv', 
                 parse_dates=[0])
df
# %%
ys = df['Closing Price (USD)']
ts = df.index

from thinkdsp import Wave, decorate

wave = Wave(ys, ts, framerate=1)
wave.plot()
decorate(xlabel='Time (days)')
# %%
spectrum = wave.make_spectrum()
spectrum.plot_power()
decorate(xlabel='Frequency (1/days)',
         ylabel='Power', 
         xscale='log', 
         yscale='log')
# %%
spectrum.estimate_slope()[0]
# %%
