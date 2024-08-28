# Keyword-Spotting-and-Voice-Recognition
This project performs  Audio File Processing, Speech-to-Text Transcription, Voice Gender Identification, Keyword Spotting, and Visualization.
Audio File Processing

The script loads an audio file using Librosa's load function, which returns two values: y (the audio time series) and sr (the sampling rate).
The mono=True parameter ensures that the audio file is converted to mono (single-channel) format, which is suitable for speech processing.
The loaded audio data is then preprocessed for further analysis.
Speech-to-Text Transcription

The script uses the SpeechRecognition library to transcribe the audio file into text.
It creates a Recognizer object, which is used to recognize speech in the audio file.
The AudioFile class is used to read the audio file, and the record method is used to record the audio data.
The recognize_google method is used to transcribe the audio data into text using Google's Speech Recognition API.
Voice Gender Identification

The script analyzes the pitch of the audio data to identify the speaker's gender (male or female).
It uses Librosa's pyin function to extract the pitch of the audio data, which returns three values: pitches, voiced_flags, and voiced_probs.
The pitch array contains the estimated pitch values, while voiced_flags and voiced_probs indicate the likelihood of each pitch value being voiced (i.e., corresponding to a spoken segment).
The script filters out unvoiced segments by selecting only the pitch values corresponding to voiced flags.
The average pitch value is then calculated, and based on a simple threshold (165 Hz), the script determines the speaker's gender: male (below 165 Hz) or female (above 165 Hz).
Keyword Spotting

The script searches for specific keywords in the transcribed text and returns their occurrences, along with timestamps.
It splits the transcribed text into individual words and calculates the average duration of each word.
For each keyword, it searches for occurrences in the transcribed text and updates a dictionary with the count and timestamps of each occurrence.
Visualization

The script plots the keyword occurrences on a waveform graph using Matplotlib.
It displays the audio waveform using Librosa's waveshow function, with the keyword occurrences marked by vertical red lines.
The x-axis represents time, and the y-axis represents amplitude.
Example Usage

The script provides an example usage at the end, where it loads an audio file named 'female3.wav', searches for the keyword 'yes', and identifies the speaker's gender.
The output includes the occurrences of the keyword 'yes' with timestamps, as well as the identified gender of the speaker.
