# %%
from thinkdsp import read_wave, decorate
# %%
# Open shot wave
response = read_wave('180960__kleeb__gunshot.wav')
start = 0.12
response = response.segment(start=start)
response.shift(-start)
response.normalize()
response.plot()
decorate(xlabel='Time (s)')
# %%
response.make_audio()
# %%
# Open violin wave
violin = read_wave('92002__jcveliz__violin-origional.wav')
start = 0.11
violin = violin.segment(start=start)
violin.shift(-start)
violin.truncate(len(response))
violin.normalize()
violin.plot()
decorate(xlabel='Time (s)')
# %%
violin.make_audio()
# %%
transfer = response.make_spectrum()
spectrum = violin.make_spectrum()
output = (spectrum * transfer).make_wave()
output.normalize()
output.plot()
output.make_audio()
# %%
response.zero_pad(len(response) * 2)
violin.zero_pad(len(violin) * 2)
# %%
violin.plot()
# %%
response.plot()
# %%
transfer = response.make_spectrum()
spectrum = violin.make_spectrum()
output = (spectrum * transfer).make_wave()
output.normalize()
output.plot()
output.make_audio()