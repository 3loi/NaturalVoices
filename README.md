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
	Figure 1. An illustration of our data sourcing pipeline with various modules. The code and dataset will be released after the review process. </font>
</figcaption>
<br>




<h2>Speech Samples Nautral Voices: </h2>

| Category           | Sample 1 | Sample 2  | Sample 3  |
|--------------------|----------|-----------|-----------|
| **Speakers**       | 1        | 2         | 4         |
|                    | [Audio](data/NV_Audios/speakers1.wav) | [Audio](data/NV_Audios/speakers2.wav) | [Audio](data/NV_Audios/speakers4.wav) |
| **SNR**            | 0        | 50        | 100       |
|                    | [Audio](data/NV_Audios/snr_0.wav) | [Audio](data/NV_Audios/snr_50.wav) | [Audio](data/NV_Audios/snr_100.wav) |
| **Emotion**        | high arousal | high dominance | high valence |
|                    | [Audio](data/NV_Audios/high_arousal.wav) | [Audio](data/NV_Audios/high_dominance.wav) | [Audio](data/NV_Audios/high_valence.wav) |
|                    | low arousal  | low dominance  | low valence  |
|                    | [Audio](data/NV_Audios/low_arousal.wav) | [Audio](data/NV_Audios/low_dominance.wav) | [Audio](data/NV_Audios/low_valence.wav) |
| **Event Classification** | Cat    | Clapping   | Sirens     |
|                    | [Audio](data/NV_Audios/cat.wav) | [Audio](data/NV_Audios/clapping.wav) | [Audio](data/NV_Audios/sirens.wav) |
| **Speech & Music** | Music   | Speech     | Music      |
|                    | [Audio](data/NV_Audios/music1.wav) | [Audio](data/NV_Audios/speech1.wav) | [Audio](data/NV_Audios/music2.wav) |


<h2>Speech Samples VC: </h2>

<h6> <b>Model:</b> TriAAN-VC[1] </h6>
<h6> <b>Vocoder:</b> Parallel WaveGAN[2] </h6>
<h6> <b>Proposed dataset:</b> NaturalVoices  </h6>

					
<br/>
<h6> The samples are from training both the model and vocoder on our NaturalVoices dataset using 80-100dB condition and two conversion scenarios
	(the conversion between seen speakers, the conversion between unseen speakers). </h6>
<br />
<h6> We provide the utterances from source speakers, denoted as <i>Source</i>,
	the utterances from target speakers, denoted as <i>Target</i>, 
	and the converted utterances, denoted as <i>Converted</i>. </h6>

<br><br><br>
    <h2> Seen to seen speakers</h2>


    
    <table >
        <tr>
			<th>Type</th>
            <th>Source</th>
            <th>Target</th>
            <th>Converted</th>
        </tr>
        <tr>
			<td> Female to Female </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/F_F_Source_from_MSP-PODCAST_2691_205_to_MSP-PODCAST_2562_338_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/F_F_Target_from_MSP-PODCAST_2691_205_to_MSP-PODCAST_2562_338_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/F_F_Converted_from_MSP-PODCAST_2691_205_to_MSP-PODCAST_2562_338_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
		
		<tr>
			<td> Female to Male </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/F_M_Source_from_MSP-PODCAST_2598_6_to_MSP-PODCAST_1356_909_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/F_M_Target_from_MSP-PODCAST_2598_6_to_MSP-PODCAST_1356_909_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/F_M_Converted_from_MSP-PODCAST_2598_6_to_MSP-PODCAST_1356_909_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
		<tr>
			<td> Male to Female </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/M_F_Source_from_MSP-PODCAST_0369_52_to_MSP-PODCAST_2612_132_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/M_F_Target_from_MSP-PODCAST_0369_52_to_MSP-PODCAST_2612_132_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/M_F_Conversion_from_MSP-PODCAST_0369_52_to_MSP-PODCAST_2612_132_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
		<tr>
			<td> Male to Male </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/M_M_Source_from_MSP-PODCAST_5324_215_to_MSP-PODCAST_1358_4_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/M_M_Target_from_MSP-PODCAST_5324_215_to_MSP-PODCAST_1358_4_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Seen_speaker_to_seen_speaker/M_M_Converted_from_MSP-PODCAST_5324_215_to_MSP-PODCAST_1358_4_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
    </table>
	
	
	<br><br><br>
	<h2> Unseen to unseen speakers</h2>
    <table >
        <tr>
			<th>Type</th>
            <th>Source</th>
            <th>Target</th>
            <th>Converted</th>
        </tr>
        <tr>
			<td> Female to Female </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/F_F_Source_from_MSP-PODCAST_0114_21_to_MSP-PODCAST_0794_263_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/F_F_Target_from_MSP-PODCAST_0114_21_to_MSP-PODCAST_0794_263_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/F_F_Converted_from_MSP-PODCAST_0114_21_to_MSP-PODCAST_0794_263_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
		
		<tr>
			<td> Female to Male </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/F_M_Source_from_MSP-PODCAST_0794_470_to_MSP-PODCAST_0230_235_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/F_M_Target_from_MSP-PODCAST_0794_470_to_MSP-PODCAST_0230_235_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/F_M_Converted_from_MSP-PODCAST_0794_470_to_MSP-PODCAST_0230_235_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
		<tr>
			<td> Male to Female </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/M_F_Source_from_MSP-PODCAST_0555_251_to_MSP-PODCAST_0114_71_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/M_F_Target_from_MSP-PODCAST_0555_251_to_MSP-PODCAST_0114_71_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/M_F_Converted_from_MSP-PODCAST_0555_251_to_MSP-PODCAST_0114_71_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
		<tr>
			<td> Male to Male </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/M_M_Source_from_MSP-PODCAST_0195_100_to_MSP-PODCAST_0292_1_src.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/M_M_Target_from_MSP-PODCAST_0195_100_to_MSP-PODCAST_0292_1_trg.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
            <td>
                <audio controls>
                    <source src="data/Unseen_speaker_to_unseen_speaker/M_M_Converted_from_MSP-PODCAST_0195_100_to_MSP-PODCAST_0292_1_cnv_gen.wav" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </td>
        </tr>
		
    </table>

    
<br><br><br>
[1] Park, Hyun Joon, et al. "TriAAN-VC: Triple Adaptive Attention Normalization for Any-to-Any Voice Conversion." ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023.
<br>
[2] Yamamoto, Ryuichi, Eunwoo Song, and Jae-Min Kim. "Parallel WaveGAN: A fast waveform generation model based on generative adversarial networks with multi-resolution spectrogram." ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020.
				</div>
	
                     
		</div>
	  </div>



                
      <hr>
      <div class="row" id="ref">
        <div class="col">
          <!--<h2>References</h2>
          
         -->
        </div>
      </div>
      <hr>

    </div>
  </main>
  <footer class="bg-secondary text-light mt-4 pt-3 pb-2 ">
    <div class="container">
      <p class="text-center">
        
      </p>
    </div>
  </footer>
  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
    integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
    integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
    crossorigin="anonymous"></script>
</body>

</html>
