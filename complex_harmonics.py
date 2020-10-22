import numpy as np
import scipy
import numpy as np
import scipy.io.wavfile as wavf
import matplotlib.pylab as plt

def wave_for(A, f):
    w = 2 * np.pi * f

    return lambda t: A * np.exp(1j * w * t)

def ifft(frequencies, amplitudes):
    def wave(t):
        waves = [ wave_for(z, f) for f, z in zip(frequencies, amplitudes) ]
        samples = [ f(t) for f in waves ]

        return np.sum(samples, axis=0).real

    return wave

if __name__ == "__main__":
    show_waveform = True

    fs = 44100
    duration = 10
    sample_count = duration * fs
    time = np.linspace(0, duration, sample_count)

    fundamental = 30
    harmonics = np.arange(1, 30, 2)
    frequencies = fundamental * harmonics
    wave = ifft(frequencies, 1j / harmonics)

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
