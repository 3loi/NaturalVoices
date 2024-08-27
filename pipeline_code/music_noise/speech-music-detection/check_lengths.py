from doctest import master
from operator import contains
import librosa
import os
import shutil


root = '/home/podcast/Desktop/MSP_Podcast_FILTER/INPUTS_OUTPUTS/Outputs/'
master_loc = root + 'Short_split_musicfilter_file/'
asr = root  + 'Short_split_musicfilter_ASR/'

out_range_dir = root + 'out_range'
os.mkdir(out_range_dir)

fnames = os.listdir(master_loc)
out_of_range = []

for fname in fnames:
    location = master_loc + '/' +  fname

    y, sr = librosa.load(location)
    duration = librosa.get_duration(y=y, sr=sr)

    if duration < 2.75:
        out_of_range.append(fname)
    elif duration > 11.009:
        out_of_range.append(fname)

for fname in out_of_range:
    shutil.move(master_loc + fname, out_range_dir + '/' + fname)
    shutil.move(asr + fname.replace('.wav','.txt'), out_range_dir + '/' + fname.replace('.wav','.txt'))


fnames = os.listdir(asr)
too_short = []
for fname in fnames:
    path_to_file = asr + fname
    with open(path_to_file) as f:
        contents = f.readlines()

    contents = contents[0].split(' ')

    if len(contents) < 5:
        too_short.append(fname.replace('.txt','.wav'))

for fname in too_short:
    shutil.move(master_loc + fname, out_range_dir + '/' + fname)
    shutil.move(asr + fname.replace('.wav','.txt'), out_range_dir + '/' + fname.replace('.wav','.txt'))