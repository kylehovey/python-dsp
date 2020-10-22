import numpy as np
from util import dft, ifft, save_waveform, plot_waveform, plot_spectrum, time_axis

if __name__ == "__main__":
    show_waveform = True
    sample_rate = 44100
    fundamental = 30
    harmonics = np.arange(1, 100, 2)
    frequencies = fundamental * harmonics
    amplitudes = 1j / harmonics
    wave = ifft(frequencies, amplitudes)

    duration = 0.1
    time = time_axis(duration, sample_rate)

    if show_waveform:
        plot_waveform(wave, duration, sample_rate)

    dft_frequencies, dft_amplitudes = dft(wave(time))

    nyquist = len(time) // 2
    frequencies_recovered = dft_frequencies[:nyquist] / duration
    amplitudes_recovered = dft_amplitudes[:nyquist]

    plot_spectrum(frequencies_recovered, amplitudes_recovered)

    wave_recovered = ifft(frequencies_recovered, amplitudes_recovered)

    if show_waveform:
        plot_waveform(wave_recovered, 0.1)
