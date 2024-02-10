# %%
from thinkdsp import read_wave, decorate

wave = read_wave('13793__soarer__north-sea.wav')
segment = wave.segment(start=0.0, duration=1.5)
spectrum = segment.make_spectrum()
segment2 = wave.segment(start=2.5, duration=1.5)
spectrum2 = segment2.make_spectrum()
loglog = dict(xscale='log', yscale='log')
# %%
from thinkdsp import Spectrum
import numpy as np

def bartlett_method(wave, seg_length=512, win_flag=True):
    # make a spectrogram and extract the spectrums
    spectro = wave.make_spectrogram(seg_length, win_flag)
    spectrums = spectro.spec_map.values()
    
    # extract the power array from each spectrum
    psds = [spectrum.power for spectrum in spectrums]
    
    # compute the root mean power (which is like an amplitude)
    hs = np.sqrt(sum(psds) / len(psds))
    fs = next(iter(spectrums)).fs
    
    # make a Spectrum with the mean amplitudes
    spectrum = Spectrum(hs, fs, wave.framerate)
    return spectrum

psd = bartlett_method(segment)
psd2 = bartlett_method(segment2)

psd.plot_power()
psd2.plot_power()

decorate(xlabel='Frequency (Hz)', 
         ylabel='Power', 
         **loglog)
# %%
