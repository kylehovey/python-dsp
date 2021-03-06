import numpy as np
import matplotlib.pylab as plt
import scipy.io.wavfile as wavf

'''
Functions for signal synthesis
'''

# Generate a uniformly sampled time axis of a given duration in seconds
def time_axis(duration, sample_rate=44100):
    sample_count = int(duration * sample_rate)

    return np.linspace(0, duration, sample_count)

# Generate a simple sinewave function for a given frequency
def sinewave(f):
    w = 2 * np.pi * f

    return lambda t: np.sin(w * t)

# Sum up sinewaves with no phase shift with a list of harmonics and their amplitudes
def harmonic_sum(fundamental, harmonics, amplitudes):
    def wave(t):
        waves = [ sinewave(f) for f in fundamental * harmonics ]
        samples = [ A * f(t) for f, A in zip(waves, amplitudes) ]

        return np.sum(samples, axis=0)

    return wave

# Generate a complex phasor with complex amplitude A and frequency f
def wave_for(A, f):
    w = 2 * np.pi * f

    return lambda t: A * np.exp(1j * w * t)

'''
Transformation functions
'''

# Create a waveform given the frequency bins and corrsponding complex amplitudes
def ifft(frequencies, amplitudes):
    def wave(t):
        waves = [ wave_for(z, f) for f, z in zip(frequencies, amplitudes) ]
        samples = [ f(t) for f in waves ]

        return np.sum(samples, axis=0).real

    return wave

def dft(samples):
    N = len(samples)

    def maker(n, k):
        return np.exp(-1j * 2 * np.pi * k * n / N)

    A = np.fromfunction(maker, (N, N))

    return np.arange(N), np.dot(A, samples)

'''
Output functions
'''

# Save a waveform to an audio file (WAV)
def save_waveform(wave, file_name, duration=10, sample_rate=44100):
    wavf.write(file_name, sample_rate, wave(time_axis(duration, sample_rate)))

# Plot a waveform visually
def plot_waveform(wave, window, sample_rate=44100):
    window_samples = time_axis(window, sample_rate)
    plt.plot(window_samples, wave(window_samples))
    plt.xlabel("time (s)")
    plt.ylabel("amplitude")
    plt.axis("tight")
    plt.show()

def plot_spectrum(frequencies, amplitudes):
    plt.plot(frequencies, np.abs(amplitudes))
    plt.xlabel("Wave number")
    plt.ylabel("Absolute amplitude")
    plt.axis("tight")
    plt.show()
