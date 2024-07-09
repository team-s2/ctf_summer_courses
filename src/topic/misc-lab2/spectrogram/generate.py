from array2gif import write_gif  # version: 1.0.4
import librosa  # version: 0.10.2.post1
import numpy  # version: 1.26.4


num_freqs = 32
quantize = 2
min_db = -60
max_db = 30
fft_window_size = 2048
frame_step_size = 512
window_function_type = 'hann'
color_pixel = (0, 0, 255)
white_pixel = (255, 255, 255)


def convert_to_gif(src, dst):
    y, sample_rate = librosa.load(src)

    spectrogram = numpy.around(  # 四舍五入
        librosa.power_to_db(
            librosa.feature.melspectrogram(
                y=y, sr=sample_rate, n_mels=num_freqs,
                n_fft=fft_window_size,
                hop_length=frame_step_size,
                window=window_function_type
            )
        ) / quantize
    ) * quantize

    gif_data = [
        numpy.kron(
            numpy.array([
                [
                    color_pixel if freq % 2 and i < round(
                        frame[freq // 2]) else white_pixel
                    for i in reversed(
                        range(min_db, max_db + 1, quantize))
                ]
                for freq in range(num_freqs * 2 + 1)
            ]),
            numpy.ones([quantize, quantize, 1])
        )
        for frame in spectrogram.transpose()
    ]

    write_gif(gif_data, dst, fps=sample_rate/frame_step_size)


if __name__ == '__main__':
    convert_to_gif('flag-1.mp3', 'flag-1.gif')  # sample rate is 44100 Hz
    convert_to_gif('flag-2.mp3', 'flag-2.gif')  # sample rate is 44100 Hz
