# %%
from thinkdsp import read_wave, decorate, TriangleSignal
import numpy as np
from matplotlib import pyplot as plt
# %%
wave = read_wave('100475__iluppai__saxophone-weep.wav')
wave.normalize()
wave.make_audio()
# %%
gram = wave.make_spectrogram(seg_length=1024)
gram.plot(high=3000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
# %%
start = 4.0
duration = 0.5
segment = wave.segment(start=start, duration=duration)
segment.make_audio()
# %%
spectrum = segment.make_spectrum()
spectrum.plot(high=3000)
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
# %%
spectrum.peaks()[:10]
# %%
TriangleSignal(freq=414).make_wave(duration=0.5).make_audio()
# %%
def autocorr(segment):
    corrs = np.correlate(segment.ys, segment.ys, mode='same')
    N = len(corrs)
    lengths = range(N, N//2, -1)

    half = corrs[N//2:].copy()
    half /= lengths
    half /= half[0]
    return half

corrs = autocorr(segment)
plt.plot(corrs[:200])
decorate(xlabel='Lag', ylabel='Correlation', ylim=[-1.05, 1.05])
# %%
def find_frequency(corrs, low, high):
    lag = np.array(corrs[low:high]).argmax() + low
    print(lag)
    period = lag / segment.framerate
    frequency = 1 / period
    return frequency

find_frequency(corrs, 80, 125)
# %%
spectrum2 = segment.make_spectrum()
spectrum2.high_pass(600)
spectrum2.plot(high=3000)
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
segment2 = spectrum2.make_wave()
segment2.make_audio()
# %%
corrs = autocorr(segment2)
plt.plot(corrs[:200])
decorate(xlabel='Lag', ylabel='Correlation', ylim=[-1.05, 1.05])
# %%
find_frequency(corrs, 80, 125)
# %%
find_frequency(corrs, 20, 50)
# %%
find_frequency(corrs, 50, 80)
# %%
spectrum4 = segment.make_spectrum()
spectrum4.high_pass(600)
spectrum4.low_pass(1200)
spectrum4.plot(high=3000)
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
# %%
spectrum4.peaks()[:5]
# %%
segment4 = spectrum4.make_wave()
segment4.make_audio()
# %%
TriangleSignal(freq=830).make_wave(duration=0.5).make_audio()
# %%
corrs = autocorr(segment4)
plt.plot(corrs[:200])
decorate(xlabel='Lag', ylabel='Correlation', ylim=[-1.05, 1.05])
# %%
find_frequency(corrs, 25, 75)
