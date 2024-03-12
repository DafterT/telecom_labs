# %%
from thinkdsp import read_wave, decorate
# %%
response = read_wave('stalbans_a_mono.wav')
duration = 5
response = response.segment(duration=duration)
response.normalize()
response.plot()
decorate(xlabel='Time (s)')
# %%
response.make_audio()
# %%
transfer = response.make_spectrum()
transfer.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
# %%
wave = read_wave('170255__dublie__trumpet.wav')
wave.truncate(len(response))
wave.normalize()
wave.plot()
decorate(xlabel='Time (s)')
# %%
wave.make_audio()
# %%
spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
# %%
output = (spectrum * transfer).make_wave()
output.normalize()
output.plot()
# %%
wave.plot()
# %%
output.make_audio()
# %%
convolved2 = wave.convolve(response)
convolved2.normalize()
convolved2.plot()
convolved2.make_audio()
# %%