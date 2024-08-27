from pathlib import Path

base_path =  Path(__file__).parent

config = {
    "cude_device": "cuda:0",
    "json_path": str(base_path.joinpath("all_data.json")),
    "whisper": {
        "model": "large-v2",
        "output_path": str(base_path.parent.joinpath("faster_whisper")),
    },
    
    "pyannote":{
        "diar_model":"pyannote/speaker-diarization-3.1",
        "vad_model": "pyannote/voice-activity-detection",
        "diar_output_path": str(base_path.parent.joinpath("pyannote")),
        "vad_output_path": str(base_path.parent.joinpath("vad")),
        "auth_key":"place_your_code_here",
    },
    
    "podcast":{
        "path": str(base_path.parent.joinpath("podcasts")),
    },
    "age_gender_model": "audeering/wav2vec2-large-robust-6-ft-age-gender",
    
    "event_classification_model":"MIT/ast-finetuned-audioset-10-10-0.4593",
    "emo_attributes":"3loi/SER-Odyssey-Baseline-WavLM-Multi-Attributes", 
}