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


download_asr
download_diarization
download_vad

exit 0
