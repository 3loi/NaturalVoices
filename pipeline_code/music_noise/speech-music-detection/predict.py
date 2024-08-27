import argparse
from smd.data import preprocessing
from smd.data import postprocessing
import smd.utils as utils
import numpy as np
import tensorflow as tf
import keras.models
from tqdm import tqdm
import os
import glob
import shutil

long_reseg = '/home/podcast/Desktop/MSP_Podcast_FILTER/INPUTS_OUTPUTS/Outputs/Long_reseg_file/'
short_split = '/home/podcast/Desktop/MSP_Podcast_FILTER/INPUTS_OUTPUTS/Outputs/Short_split_file/'

longs = os.listdir(long_reseg)

for flong in longs:
    source = long_reseg + flong
    destination = short_split + flong
    shutil.move(source, destination)

long_asr = '/home/podcast/Desktop/MSP_Podcast_FILTER/INPUTS_OUTPUTS/Outputs/Long_split_ASR/'
short_asr = '/home/podcast/Desktop/MSP_Podcast_FILTER/INPUTS_OUTPUTS/Outputs/Short_split_ASR/'

for flong in longs:
    source = long_asr + flong[:21] + '.txt'
    destination = short_asr + flong.replace('.wav','.txt')
    shutil.copy(source, destination)

os.rmdir('/home/podcast/Desktop/MSP_Podcast_FILTER/INPUTS_OUTPUTS/Outputs/Long_reseg_file')



def test_data_processing(file, mean, std):
    if os.path.splitext(file)[1] == '.npy':
        spec = np.load(file)
    else:
        audio = utils.load_audio(file)
        spec = preprocessing.get_spectrogram(audio)
    mels = preprocessing.get_scaled_mel_bands(spec)
    mels = preprocessing.normalize(mels, mean, std)
    return mels.T


def predict(data_path, output_file, model_path, mean_path, std_path, smoothing):
    mean = np.load(mean_path)
    std = np.load(std_path)

    print("Loading the model " + model_path + "..")
    with tf.device('/cpu:0'):
        model = keras.models.load_model(model_path)
    print("Start the prediction..")

    if os.path.isdir(data_path):
        if output_file != "":
            raise ValueError("It is possible to set an output file only if the input is a file.")

        files = glob.glob(os.path.abspath(data_path) + "/*.npy") + glob.glob(os.path.abspath(data_path) + "/*.wav")
        for file in tqdm(files):
            x = test_data_processing(file, mean, std)
            x = x.reshape((1, x.shape[0], x.shape[1]))
            output = model.predict(x, batch_size=1, verbose=0)[0].T
            output = postprocessing.apply_threshold(output)
            if smoothing:
                output = postprocessing.smooth_output(output)
            annotation = preprocessing.label_to_annotation(output)
            output_path = file.replace(".npy", '') + "_prediction.txt"
            output_path = output_path.replace('.wav','')
            utils.save_annotation(annotation, output_path)
    else:
        file = os.path.abspath(data_path)
        x = test_data_processing(file, mean, std)
        x = x.reshape((1, x.shape[0], x.shape[1]))
        output = model.predict(x, batch_size=1, verbose=0)[0].T
        output = postprocessing.apply_threshold(output)
        if smoothing:
            output = postprocessing.smooth_output(output)
        annotation = preprocessing.label_to_annotation(output)
        if output_file != "":
            output_path = output_file
        else:
            output_path = file.replace(".npy", '') + "_prediction.txt"
            output_path = output_path.replace('.wav','')
        utils.save_annotation(annotation, output_path)

root = '/home/podcast/Desktop/MSP_Podcast_FILTER/'

output_location = 'INPUTS_OUTPUTS/Outputs/'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to do the prediction with a neural network for the speech and music detection task.")

    parser.add_argument('--data_path', type=str, default=root + output_location + "Short_split_file/",
                        help='path to a file or a folder for prediction')

    parser.add_argument('--output_file', type=str, default="",
                        help='set a name for a precise output file')

    parser.add_argument('--model', type=str, default=root + "speech-music-detection/checkpoint/weights.28-0.13exp1_blstm.hdf5",
                        help='path of the model to load when the starting is resumed')

    parser.add_argument('--mean_path', type=str, default=root + "speech-music-detection/checkpoint/mean_gtzan_esc-50_muspeak_musan.npy",
                        help='path of the mean of the normalization applied with the model')

    parser.add_argument('--std_path', type=str, default=root + "speech-music-detection/checkpoint/std_gtzan_esc-50_muspeak_musan.npy",
                        help='path of the std of the normalization applied with the model')

    parser.add_argument('--smoothing', type=bool, default=True,
                        help='true or false, apply to smoothing function to the ouput')

    args = parser.parse_args()

    predict(args.data_path, args.output_file, args.model, args.mean_path, args.std_path, args.smoothing)
