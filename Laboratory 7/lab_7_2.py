# %%
import numpy as np
import matplotlib.pyplot as plt
PI2 = 2 * np.pi
# %%
ys = [-0.5, 0.1, 0.7, -0.1]
hs = np.fft.fft(ys)
hs
# %%
def fft_norec(ys):
    N = len(ys)
    He = np.fft.fft(ys[::2])
    Ho = np.fft.fft(ys[1::2])
    
    ns = np.arange(N)
    W = np.exp(-1j * PI2 * ns / N)
    
    return np.tile(He, 2) + W * np.tile(Ho, 2)

hs1 = fft_norec(ys)
np.sum(np.abs(hs - hs1))
# %%
def my_fft(ys):
    N = len(ys)
    if N == 1:
        return ys
    
    He = my_fft(ys[::2])
    Ho = my_fft(ys[1::2])
    
    ns = np.arange(N)
    W = np.exp(-1j * PI2 * ns / N)
    
    return np.tile(He, 2) + W * np.tile(Ho, 2)

hs2 = my_fft(ys)
np.sum(np.abs(hs - hs2))
# %%
def dft(ys):
    N = len(ys)
    ts = np.arange(N) / N
    freqs = np.arange(N)
    args = np.outer(ts, freqs)
    M = np.exp(1j * PI2 * args)
    amps = M.conj().transpose().dot(ys)
    return amps

hs3 = dft(ys)
np.sum(np.abs(hs - hs3))
# %%
def run_speed_test(func, lengths, ys):
    bests = []
    print(func.__name__)
    for l in lengths:
        print(l)
        result = %timeit -r1 -o func(ys[:l])
        bests.append(result.best)

    return bests

def generate_ys(max_length=2**5):
    return np.random.uniform(-1, 1, max_length)
# %%
max_length = 15
lengths = [2 ** i for i in range(5, max_length)]
ys = generate_ys(lengths[-1])
# %%
fft_res = run_speed_test(np.fft.fft, lengths, ys)
# %%
dft_res = run_speed_test(dft, lengths, ys)
# %%
my_fft_res = run_speed_test(my_fft, lengths, ys)
# %%
from scipy.stats import linregress

def plot_speed_test(lengths, ys, label):
    plt.plot(lengths, ys, label=label)
    x = np.log(lengths)
    y = np.log(ys)
    t = linregress(x,y)
    print(label, t[0])

plot_speed_test(lengths, fft_res, 'fft')
plot_speed_test(lengths, dft_res, 'dft')
plot_speed_test(lengths, my_fft_res, 'my_fft')

plt.legend()
plt.xlabel('Len')
plt.ylabel('Time (s)')
plt.xscale('log')
plt.yscale('log')
# %%
