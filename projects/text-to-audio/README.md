# Text-to-Speech Project Using AWS Lambda and Polly

## Audio Output

🎧 [Download audio sample](./Sample-Audio.mp3)  
*(Right-click and choose "Save link as..." to download)*


## Project Overview
This project converts text to speech using AWS Lambda and Amazon Polly. It automates the process of transforming book chapters or any text into audio files stored in AWS S3.

## Features
- Converts text input into speech audio files.
- Uploads generated audio files to an S3 bucket.
- Handles text splitting to avoid AWS service limits.

## AWS Technologies Used
- AWS Lambda (serverless function)
- Amazon Polly (text-to-speech service)
- Amazon S3 (storage for audio files)

## How to Use
1. Upload your text files to the designated S3 bucket.
2. Trigger the Lambda function to process the text.
3. Generated MP3 audio files are saved back to S3.

## Limitations
- Text length is limited per request, so the input is split into manageable chunks.
- Currently supports only specific languages available in Polly.

## Possible Improvements
- Add support for more languages and voices.
- Integrate with a web interface for easier usage.
- Implement real-time streaming of audio.

## Example Files
Included are sample text inputs and resulting MP3 files demonstrating the audio quality.
