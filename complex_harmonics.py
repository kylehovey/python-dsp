import numpy as np
from util import wave_for, ifft, plot_waveform, save_waveform

if __name__ == "__main__":
    show_waveform = True
    fundamental = 30
    harmonics = np.arange(1, 30, 2)
    frequencies = fundamental * harmonics
    wave = ifft(frequencies, 1j / harmonics)

    save_waveform(wave, "out.wav")

    if show_waveform:
        plot_waveform(wave, 0.1)
