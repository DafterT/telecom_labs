# %%
from thinkdsp import TriangleSignal

triangle = TriangleSignal().make_wave(duration=0.01)
triangle.plot()
# %%
spectrum = triangle.make_spectrum()
spectrum.hs[0]
# %%
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
# %%
