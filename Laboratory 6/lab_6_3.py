# %%
import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate, PI2, read_wave
# %%
from thinkdsp import SawtoothSignal

signal = SawtoothSignal(freq=500, offset=0)
wave = signal.make_wave(duration=0.5, framerate=40000)
wave.segment(duration=0.01).plot()
decorate(xlabel='Time (s)')
wave.make_audio()
# %%
spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)',
         ylabel='Amplitude')
# %%
def plot_angle(spectrum, thresh=1):
    angles = spectrum.angles
    angles[spectrum.amps < thresh] = np.nan
    plt.plot(spectrum.fs, angles, 'x')
    decorate(xlabel='Frequency (Hz)', 
             ylabel='Phase (radian)')

plot_angle(spectrum, thresh=0)
# %%
plot_angle(spectrum, thresh=1)
# %%
def plot_three(spectrum, thresh=1):
    plt.figure(figsize=(10, 4))
    plt.subplot(1,3,1)
    spectrum.plot()
    plt.subplot(1,3,2)
    plot_angle(spectrum, thresh=thresh)
    plt.subplot(1,3,3)
    wave = spectrum.make_wave()
    wave.unbias()
    wave.normalize()
    wave.segment(duration=0.01).plot()
    display(wave.make_audio())

plot_three(spectrum)
# %%
def zero_angle(spectrum):
    res = spectrum.copy()
    res.hs = res.amps
    return res
spectrum2 = zero_angle(spectrum)
plot_three(spectrum2)
# %%
def rotate_angle(spectrum, offset):
    res = spectrum.copy()
    res.hs *= np.exp(1j * offset)
    return res

spectrum3 = rotate_angle(spectrum, 1)
plot_three(spectrum3)
# %%
def random_angle(spectrum):
    res = spectrum.copy()
    angles = np.random.uniform(0, PI2, len(spectrum))
    res.hs *= np.exp(1j * angles)
    return res
spectrum4 = random_angle(spectrum)
plot_three(spectrum4)
# %%
wave = read_wave('code_120994__thirsk__120-oboe.wav')
wave.make_audio()
# %%
segment = wave.segment(start=1.1, duration=0.9)
spectrum = segment.make_spectrum()
plot_three(spectrum, thresh=50)
# %%
spectrum2 = zero_angle(spectrum)
plot_three(spectrum2, thresh=50)
# %%
spectrum3 = rotate_angle(spectrum, 1)
plot_three(spectrum3, thresh=50)
# %%
spectrum4 = random_angle(spectrum)
plot_three(spectrum4, thresh=50)
# %%
wave = read_wave('code_100475__iluppai__saxophone-weep.wav')
wave.make_audio()
segment = wave.segment(start=3.5, duration=0.6)
# %%
spectrum = segment.make_spectrum()
plot_three(spectrum, thresh=50)
# %%
spectrum2 = zero_angle(spectrum)
plot_three(spectrum2, thresh=50)
# %%
spectrum3 = rotate_angle(spectrum, 1)
plot_three(spectrum3, thresh=50)
# %%
spectrum4 = random_angle(spectrum)
plot_three(spectrum4, thresh=50)
# %%
spectrum.high_pass(600)
spectrum.plot(high=4000)
# %%
plot_three(spectrum, thresh=50)
# %%
spectrum2 = zero_angle(spectrum)
plot_three(spectrum2, thresh=50)
# %%
spectrum3 = rotate_angle(spectrum, 1)
plot_three(spectrum3, thresh=50)
# %%
spectrum4 = random_angle(spectrum)
plot_three(spectrum4, thresh=50)
# %%
