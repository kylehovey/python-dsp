import numpy as np
from util import sinewave, harmonic_sum, plot_waveform, save_waveform

if __name__ == "__main__":
    show_waveform = True
    fundamental = 100
    harmonics = np.arange(1, 100, 2)
    wave = harmonic_sum(100, harmonics, 1.0 / harmonics)

    save_waveform(wave, "out.wav")

    if show_waveform:
        plot_waveform(wave, 0.1)
