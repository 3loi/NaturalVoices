
Note that this repository is currently being updated regularly. We aim to finalize the repository before the InterSpeech 2024 conference. If you have any questions, feel free to open a discussion in "Issues".


# NaturalVoices Dataset & Pipeline


NaturalVoices introduces a novel data-sourcing pipeline alongside the release of a new natural speech dataset for voice conversion (VC). This pipeline leverages proven, high-performance techniques to extract detailed information such as Automatic Speech Recognition (ASR), speaker diarization, and signal-to-noise ratio (SNR) from raw podcast data. Using the pipeline we create a large-scale, spontaneous, expressive, and emotionally rich speech dataset tailored for VC applications. Objective and subjective evaluations demonstrate the effectiveness of using our pipeline for providing natural and expressive data for VC.



<h2>Pipeline Architecture: </h2>

![alt text](./data/pipeline.png)
<figcaption style="text-align:center;"></font><font size=3> 
	The above image is an illustration of our data sourcing pipeline with various modules. </font>
</figcaption>
<br><br>


To see an overview of audio segments visit the Pages website [[website](https://3loi.github.io/NaturalVoices/)].

---------------------------

### Downloading the audios

The audio files are zipped and uploaded in batches. Each zip file can be unzipped individually and is around 40GB so please ensure you have sufficient storage space and be patient, as the download process may take some time.


The audios will be saved in the `audios_zipped` in working directory. To automatically download all the zipped files, please run the following command: 
  ```
  $ bash download_audios.sh
  ```

If you wish to manually download a file, please visit this [[website](https://lab-msp.com/NaturalVoices/audios_16khz)].

---------------------------

### Downloading the meta-data

The meta-data contains the output of running Faster-Whisper, PyAnnote (Diarization + Voice Activity Detection + Speaker Overlap). 

To download the meta-data run the following command:
  ```
  $ bash download_meta.sh
  ```

If you wish to manually download a file, please visit this [[website](https://lab-msp.com/NaturalVoices)].

---------------------------

### File Structure

After downloading all the files, you should have the following file structure:

```
NaturalVoices
	vad
		MSP-PODCAST_0001
		...
	pyannote
		MSP-PODCAST_0001
		...
	faster-whisper
		MSP-PODCAST_0001
		...

```



---------------------------

For an example on how to open and show the meta-data please open the [example_code](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/example_code.ipynb) file. In summary: Each file inside the directories is a pickle file that can be loaded in Python using the following code:

```
def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        data =  pickle.load(f)
    return data
```

---------------------------

# Running the pipeline
The code used to generate the labels is located in [pieline_code](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code). There are three main steps we used to generate the labels.

1. Run the podcast level code
    - This includes models that predict on the whole audio files
    - [faster_whisper](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/faster_whisper.ipynb), [pyannote_diarization.ipynb](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/pyannote_diarization.ipynb), [vad.ipynb](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/vad.ipynb)
3. Create the utterances
    - This step uses the segments from whisper to define the utterances
    - [generate_utt](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/generate_utt.ipynb) 
5. Run the utterance level code
    - This step contains all remaining predictions
    - [age_gender](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/age_detector/age_detector.ipynb), [emotional_attributes](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/emotions/pred_emo_attributes.ipynb), [emotional_categories](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/emotions/pred_emo_categorical.ipynb), [gender](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/gender-filter/gender_filter.ipynb), [SNR](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/music_noise/SNR.ipynb), [event_classification](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/music_noise/event_classification.ipynb), [speech_music](https://github.com/3loi/NaturalVoices/blob/main/pipeline_code/music_noise/speech_music_predict.ipynb)


---------------------------

  #### TODO 
  - [x] Upload 16KHz raw audio
  - [x] Upload ASR output (Faster-Whisper)
  - [x] Upload Diarization output (PyAnnote)
  - [x] Upload Voice Activity Detection output (PyAnnote)
  - [x] Upload speaker overlap output (PyAnnote)
  - [ ] Upload Gender & Age info
  - [ ] Upload Signal-to-Noise ratio
  - [ ] Upload Categorical and Attribute based emotion prediction
  - [ ] Upload Sound Event predictions
  - [x] Upload the pipeline code

---------------------------

To cite this work, please use the following BibTeX entry:

```
@InProceedings{Salman_2024,
            author={A. N. Salman and Z. Du and S. S. Chandra and I. R. Ulgen and and C. Busso and B. Sisman},
            title={Towards Naturalistic Voice Conversion: NaturalVoices Dataset with an Automatic Processing Pipeline},
            booktitle={Interspeech 2024},
            volume={},
            year={2024},
            month={September},
            address =  {Kos Island, Greece},
}
```
