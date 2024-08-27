#!/bin/bash

download_asr() {
    echo "Downloading asr data"
    wget https://lab-msp.com/NaturalVoices/faster_whisper.zip
    unzip faster_whisper.zip
    rm faster_whisper.zip
}


download_diarization() {
    echo "Downloading diarization data"
    wget https://lab-msp.com/NaturalVoices/pyannote.zip
    unzip pyannote.zip
    rm pyannote.zip
}

download_vad() {
    echo "Downloading voice activity detection data"
    wget https://lab-msp.com/NaturalVoices/vad.zip
    unzip vad.zip
    rm vad.zip
}

download_overlap() {
    echo "Downloading speaker overlap data"
    wget https://lab-msp.com/NaturalVoices/pyannote_overlap.zip
    unzip pyannote_overlap.zip
    rm pyannote_overlap.zip
}

download_utt() {
    echo "Downloading the utterance data"
    wget https://lab-msp.com/NaturalVoices/all_data.json
}




download_utt
download_asr
download_diarization
download_vad
download_overlap

exit 0
