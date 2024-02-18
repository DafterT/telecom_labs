# %%
from matplotlib import pyplot as plt
from thinkdsp import read_wave, decorate
from autocorr import autocorr
import numpy as np
# %%
wave = read_wave('28042__bcjordan__voicedownbew.wav')
wave.normalize()
# Создаем спектрограмму
spectro = wave.make_spectrogram(seg_length=1024)
spectro.plot(high=4200)
decorate(xlabel='Time (s)', 
        ylabel='Frequency (Hz)')
wave.make_audio()
# %%
def estimate_fundamental(wave, start, duration=0.01, low = 50, high = 150):
    segment = wave.segment(start=start, duration=duration)
    lags, corrs = autocorr(segment)
    lag = np.array(corrs[low:high]).argmax() + low
    return 1 / (lag / segment.framerate)

x = np.arange(0, wave.duration, 0.05)
y = [estimate_fundamental(wave, start) for start in x]
plt.plot(x, y)
decorate(xlabel='Time (s)', 
        ylabel='Frequency (Hz)')
# %%
plt.plot(x, y, color='white')
spectro.plot(high=4200)
decorate(xlabel='Time (s)', 
        ylabel='Frequency (Hz)')
# %%
