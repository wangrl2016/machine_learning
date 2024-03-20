import matplotlib.pyplot as plt
import numpy as np
import scipy

if __name__ == '__main__':
    sample_rate, data = scipy.io.wavfile.read('res/mid_tom.wav')

    if len(data.shape) > 1:
        data = data[:, 0]

    # Compute the time axis for plotting
    time = np.arange(0, len(data)) / sample_rate

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(time, data, color='black')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform')
    plt.grid(True)
    plt.show()
