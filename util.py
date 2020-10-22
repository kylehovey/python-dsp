import numpy as np
import matplotlib.pylab as plt
import scipy.io.wavfile as wavf

def time_axis(duration, sample_rate=44100):
    sample_count = duration * sample_rate

    return np.linspace(0, duration, sample_count)

def wave_for(A, f):
    w = 2 * np.pi * f

    return lambda t: A * np.exp(1j * w * t)

def sinewave(f):
    w = 2 * np.pi * f

    return lambda t: np.sin(w * t)

def harmonic_sum(fundamental, harmonics, amplitudes):
    def wave(t):
        waves = [ sinewave(f) for f in fundamental * harmonics ]
        samples = [ A * f(t) for f, A in zip(waves, amplitudes) ]

        return np.sum(samples, axis=0)

    return wave

def ifft(frequencies, amplitudes):
    def wave(t):
        waves = [ wave_for(z, f) for f, z in zip(frequencies, amplitudes) ]
        samples = [ f(t) for f in waves ]

        return np.sum(samples, axis=0).real

    return wave

def save_waveform(wave, file_name, duration=10, sample_rate=44100):
    wavf.write(file_name, sample_rate, wave(time_axis(duration, sample_rate)))

def plot_waveform(wave, window, sample_rate=44100):
    window_samples = np.linspace(0, window, sample_rate * window)
    plt.plot(window_samples, wave(window_samples))
    plt.xlabel("time (s)")
    plt.ylabel("amplitude")
    plt.axis("tight")
    plt.show()
