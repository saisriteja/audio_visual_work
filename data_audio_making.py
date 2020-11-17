import matplotlib.pyplot as plt
import librosa
import os
from librosa import display
import numpy as np

file_names = []

for root, dirs, files in os.walk("AudioData/"):
    for file in files:
        if file.endswith(".wav"):
            # print(os.path.join(root, file))
            file_names.append(os.path.join(root, file))



def make_spectrogram(filename):
    x, sr = librosa.load(filename)

    person,ff = filename.split('/')[1].split('\\')

    name = 'data_audio/'+person+'_'+ff[:-4]


    plt.figure(figsize=(12, 4))
    ax = plt.axes()
    ax.set_axis_off()
    # plt.set_cmap('hot')

    S = librosa.feature.melspectrogram(y=x, sr=sr, n_mels=128,fmax=8000)

    S_dB = librosa.power_to_db(S, ref=np.max)

    librosa.display.specshow(S_dB, y_axis='mel', x_axis='time',sr=sr,cmap='magma',fmax=8000)
    # l1,l2 = (0,4000)
    # plt.ylim(l1,l2)
    # plt.colorbar()
    plt.savefig(f'{name}.png', bbox_inches='tight', transparent=True, pad_inches=0.0 )
    # print(done)
    plt.close()

from tqdm import tqdm

for i in tqdm(file_names):
    make_spectrogram(i)

    # break