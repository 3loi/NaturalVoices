<h1>Towards More Naturalistic Voice Conversion: Introducing the NaturalVoices Dataset with an Automatic Processing Pipeline. </h1>

<h3>The code and dataset will be released soon.</h3>

Voice conversion (VC) research traditionally depends on scripted or acted speech, which lacks the natural spontaneity of real-life conversations. 
While natural speech data is limited for VC, our study focuses on filling in this gap. We introduce a novel data-sourcing pipeline that makes the 
release of a natural speech dataset for VC, named NaturalVoices. The pipeline extracts rich information in speech such as emotion and signal-to-noise 
ratio (SNR) from raw podcast data, utilizing recent deep learning methods and providing flexibility and ease of use. NaturalVoices marks a large-scale, 
spontaneous, expressive, and emotional speech dataset, comprising over 4,000 hours speech sourced from the original podcasts in the MSP-Podcast dataset. 
Objective and subjective evaluations demonstrate the effectiveness of using our pipeline for providing natural and expressive data for VC, suggesting the 
potential of NaturalVoices for broader speech generation tasks.
<br/> <br/>


<h2>Pipeline Architecture: </h2>

![alt text](./data/pipeline.png)
<figcaption style="text-align:center;"></font><font size=3> 
	Figure 1. An illustration of our data sourcing pipeline with various modules. </font>
</figcaption>
<br>




<h2>Speech Samples Nautral Voices: </h2>


| **Speakers**       | 1        | 2         | 4         |
|--------------------|----------|-----------|-----------|
|                    | [Audio](data/NV_Audios/speakers1.wav) | [Audio](data/NV_Audios/speakers2.wav) | [Audio](data/NV_Audios/speakers4.wav) |

| **SNR**            | 0        | 50        | 100       |
|--------------------|----------|-----------|-----------|
|                    | [Audio](data/NV_Audios/snr_0.wav) | [Audio](data/NV_Audios/snr_50.wav) | [Audio](data/NV_Audios/snr_100.wav) |

| **Emotion**        | high arousal | high dominance | high valence |
|--------------------|----------|-----------|-----------|
|                    | [Audio](data/NV_Audios/high_arousal.wav) | [Audio](data/NV_Audios/high_dominance.wav) | [Audio](data/NV_Audios/high_valence.wav) |
|                    | low arousal  | low dominance  | low valence  |
|                    | [Audio](data/NV_Audios/low_arousal.wav) | [Audio](data/NV_Audios/low_dominance.wav) | [Audio](data/NV_Audios/low_valence.wav) |

| **Event Classification** | Cat    | Clapping   | Sirens     |
|--------------------|----------|-----------|-----------|
|                    | [Audio](data/NV_Audios/cat.wav) | [Audio](data/NV_Audios/clapping.wav) | [Audio](data/NV_Audios/sirens.wav) |

| **Speech & Music** | Music   | Speech     | Music      |
|--------------------|----------|-----------|-----------|
|                    | [Audio](data/NV_Audios/music1.wav) | [Audio](data/NV_Audios/speech1.wav) | [Audio](data/NV_Audios/music2.wav) |


## Speech Samples VC:

#### **Model:** TriAAN-VC[1]
#### **Vocoder:** Parallel WaveGAN[2]
#### **Proposed dataset:** NaturalVoices

The samples are from training both the model and vocoder on our NaturalVoices dataset using 80-100dB condition and two conversion scenarios (the conversion between seen speakers, the conversion between unseen speakers).

We provide the utterances from source speakers, denoted as *Source*, the utterances from target speakers, denoted as *Target*, and the converted utterances, denoted as *Converted*.


<br>

### Seen to seen speakers

| Type              | Source                                                                                                              | Target                                                                                                              | Converted                                                                                                            |
|-------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Female to Female  | [Audio](data/Seen_speaker_to_seen_speaker/F_F_Source_from_MSP-PODCAST_2691_205_to_MSP-PODCAST_2562_338_src.wav)     | [Audio](data/Seen_speaker_to_seen_speaker/F_F_Target_from_MSP-PODCAST_2691_205_to_MSP-PODCAST_2562_338_trg.wav)     | [Audio](data/Seen_speaker_to_seen_speaker/F_F_Converted_from_MSP-PODCAST_2691_205_to_MSP-PODCAST_2562_338_cnv_gen.wav) |
| Female to Male    | [Audio](data/Seen_speaker_to_seen_speaker/F_M_Source_from_MSP-PODCAST_2598_6_to_MSP-PODCAST_1356_909_src.wav)       | [Audio](data/Seen_speaker_to_seen_speaker/F_M_Target_from_MSP-PODCAST_2598_6_to_MSP-PODCAST_1356_909_trg.wav)       | [Audio](data/Seen_speaker_to_seen_speaker/F_M_Converted_from_MSP-PODCAST_2598_6_to_MSP-PODCAST_1356_909_cnv_gen.wav)  |
| Male to Female    | [Audio](data/Seen_speaker_to_seen_speaker/M_F_Source_from_MSP-PODCAST_0369_52_to_MSP-PODCAST_2612_132_src.wav)      | [Audio](data/Seen_speaker_to_seen_speaker/M_F_Target_from_MSP-PODCAST_0369_52_to_MSP-PODCAST_2612_132_trg.wav)      | [Audio](data/Seen_speaker_to_seen_speaker/M_F_Conversion_from_MSP-PODCAST_0369_52_to_MSP-PODCAST_2612_132_cnv_gen.wav) |
| Male to Male      | [Audio](data/Seen_speaker_to_seen_speaker/M_M_Source_from_MSP-PODCAST_5324_215_to_MSP-PODCAST_1358_4_src.wav)       | [Audio](data/Seen_speaker_to_seen_speaker/M_M_Target_from_MSP-PODCAST_5324_215_to_MSP-PODCAST_1358_4_trg.wav)       | [Audio](data/Seen_speaker_to_seen_speaker/M_M_Converted_from_MSP-PODCAST_5324_215_to_MSP-PODCAST_1358_4_cnv_gen.wav)  |

### Unseen to Unseen Speakers

| Type              | Source                                                                                                              | Target                                                                                                              | Converted                                                                                                            |
|-------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Female to Female  | [Audio](data/Unseen_speaker_to_unseen_speaker/F_F_Source_from_MSP-PODCAST_0114_21_to_MSP-PODCAST_0794_263_src.wav)  | [Audio](data/Unseen_speaker_to_unseen_speaker/F_F_Target_from_MSP-PODCAST_0114_21_to_MSP-PODCAST_0794_263_trg.wav)  | [Audio](data/Unseen_speaker_to_unseen_speaker/F_F_Converted_from_MSP-PODCAST_0114_21_to_MSP-PODCAST_0794_263_cnv_gen.wav) |
| Female to Male    | [Audio](data/Unseen_speaker_to_unseen_speaker/F_M_Source_from_MSP-PODCAST_0794_470_to_MSP-PODCAST_0230_235_src.wav) | [Audio](data/Unseen_speaker_to_unseen_speaker/F_M_Target_from_MSP-PODCAST_0794_470_to_MSP-PODCAST_0230_235_trg.wav) | [Audio](data/Unseen_speaker_to_unseen_speaker/F_M_Converted_from_MSP-PODCAST_0794_470_to_MSP-PODCAST_0230_235_cnv_gen.wav) |
| Male to Female    | [Audio](data/Unseen_speaker_to_unseen_speaker/M_F_Source_from_MSP-PODCAST_0555_251_to_MSP-PODCAST_0114_71_src.wav)  | [Audio](data/Unseen_speaker_to_unseen_speaker/M_F_Target_from_MSP-PODCAST_0555_251_to_MSP-PODCAST_0114_71_trg.wav)  | [Audio](data/Unseen_speaker_to_unseen_speaker/M_F_Converted_from_MSP-PODCAST_0555_251_to_MSP-PODCAST_0114_71_cnv_gen.wav) |
| Male to Male      | [Audio](data/Unseen_speaker_to_unseen_speaker/M_M_Source_from_MSP-PODCAST_0195_100_to_MSP-PODCAST_0292_1_src.wav)   | [Audio](data/Unseen_speaker_to_unseen_speaker/M_M_Target_from_MSP-PODCAST_0195_100_to_MSP-PODCAST_0292_1_trg.wav)   | [Audio](data/Unseen_speaker_to_unseen_speaker/M_M_Converted_from_MSP-PODCAST_0195_100_to_MSP-PODCAST_0292_1_cnv_gen.wav)  |


    
```
[1] Park, Hyun Joon, et al. "TriAAN-VC: Triple Adaptive Attention Normalization for Any-to-Any Voice Conversion." ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023.
[2] Yamamoto, Ryuichi, Eunwoo Song, and Jae-Min Kim. "Parallel WaveGAN: A fast waveform generation model based on generative adversarial networks with multi-resolution spectrogram." ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020.
```
