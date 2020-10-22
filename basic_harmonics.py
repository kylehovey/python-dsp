import scipy
import numpy as np
import scipy.io.wavfile as wavf
import matplotlib.pylab as plt

def sinewave(f):
    w = 2 * np.pi * f

    return lambda t: np.sin(w * t)

def harmonic_sum(fundamental, harmonics, amplitudes):
    def wave(t):
        waves = [ sinewave(f) for f in fundamental * harmonics ]
        samples = [ A * f(t) for f, A in zip(waves, amplitudes) ]

        return np.sum(samples, axis=0)

    return wave

if __name__ == "__main__":
    show_waveform = True

    fs = 44100
    duration = 10
    sample_count = duration * fs
    time = np.linspace(0, duration, sample_count)

    harmonics = np.arange(1, 100, 2)
    wave = harmonic_sum(100, harmonics, np.array([ 1.0/k for k in harmonics ]) / 1.2)

    out_f = "out.wav"

    wavf.write(out_f, fs, wave(time))

    if show_waveform:
        window = 0.1
        window_samples = np.linspace(0, window, sample_count * window)
        plt.plot(window_samples, wave(window_samples))
        plt.xlabel("time (s)")
        plt.ylabel("amplitude")
        plt.axis("tight")
        plt.show()
