#!/bin/bash

# Array of URLs (zipped podcasts) to download
urls=(
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_1.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_2.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_3.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_4.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_5.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_6.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_7.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_8.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_9.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_10.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_11.zip"
    "https://lab-msp.com/NaturalVoices/audios_16khz/MSP_PODCAST_ZIP_12.zip"
)

# Directory to save downloaded zipped files
download_dir="./audios_zipped"

# Create download directory if it doesn't exist
echo "Creating $download_dir if it doesn't exist to download zipped files to"
mkdir -p "$download_dir"


echo "The total size of the zipped files exceeds 600GB. Please ensure you have sufficient free storage space and be patient, as the download process may take some time"
# Iterate through and download each zipped file
for url in "${urls[@]}"; do
    file_name=$(basename "$url")
    echo "Downloading $file_name"
    curl -o "$download_dir/$file_name" "$url"
    echo "$file_name has been downloaded and saved to $download_dir"
done

echo "All files have been downloaded."
