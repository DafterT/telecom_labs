# %%
import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate, PI2
# %%
from thinkdsp import UncorrelatedGaussianNoise

signal = UncorrelatedGaussianNoise()
noise = signal.make_wave(duration=1.0, framerate=16384)

noise.plot()
# %%
from scipy.stats import linregress

loglog = dict(xscale='log', yscale='log')

def plot_bests(ns, bests):    
    plt.plot(ns, bests)
    decorate(**loglog)
    
    x = np.log(ns)
    y = np.log(bests)
    t = linregress(x,y)
    slope = t[0]

    return slope
# %%
def run_speed_test(ns, func):
    results = []
    for N in ns:
        print(N)
        ts = (0.5 + np.arange(N)) / N
        freqs = (0.5 + np.arange(N)) / 2
        ys = noise.ys[:N]
        result = %timeit -r1 -o func(ys, freqs, ts)
        results.append(result)
        
    bests = [result.best for result in results]
    return bests

# %%
def analyze1(ys, fs, ts):
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    amps = np.linalg.solve(M, ys)
    return amps
# %%
ns = np.array(2 ** np.arange(6, 13), np.int64)
ns
# %%
bests = run_speed_test(ns, analyze1)
plot_bests(ns, bests)
# %%
def analyze2(ys, fs, ts):
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    amps = np.dot(M, ys) / 2
    return amps
# %%
bests2 = run_speed_test(ns, analyze2)
plot_bests(ns, bests2)
# %%
import scipy.fftpack

def scipy_dct(ys, fs, ts):
    return scipy.fftpack.dct(ys, type=2)
# %%
bests3 = run_speed_test(ns, scipy_dct)
plot_bests(ns, bests3)
# %%
plt.plot(ns, bests, label='analyze1')
plt.plot(ns, bests2, label='analyze2')
plt.plot(ns, bests3, label='fftpack.dct')
decorate(xlabel='Wave length (N)', ylabel='Time (s)', **loglog)
# %%
