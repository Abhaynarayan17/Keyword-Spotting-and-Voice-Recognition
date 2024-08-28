"""
Keyword-Spotting and Voice-Recognition
Automatically generated by Colab.
Original file is located at
    https://colab.research.google.com/drive/1cmkUSGWf_65uKjd4ynmCj5cHG541A-1S
"""

pip install librosa SpeechRecognition

import librosa
import speech_recognition as sr

import numpy as np
import matplotlib.pyplot as plt

# Load and preprocess the audio file
def load_audio(file_path):
    y, sr = librosa.load(file_path, mono=True)
    return y, sr

# Transcribe audio using SpeechRecognition
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

# Improved voice gender identification based on pitch
def identify_gender(audio_data, sr):
    fmin = librosa.note_to_hz('C2')
    fmax = librosa.note_to_hz('C6')
    pitches, voiced_flags, voiced_probs = librosa.pyin(audio_data, fmin=fmin, fmax=fmax)
    valid_pitches = pitches[voiced_flags]  # Filter out unvoiced segments
    if len(valid_pitches) == 0:
        return 'Unknown'
    avg_pitch = np.mean(valid_pitches)
    # Typical pitch ranges for male and female voices (simplified)
    if avg_pitch < 165:
        return 'Male'
    else:
        return 'Female'

# Main function to perform keyword spotting and gender identification
def keyword_spotting_and_gender_identification(audio_file, keywords):
    y, sr = load_audio(audio_file)
    transcription = transcribe_audio(audio_file)
    gender = identify_gender(y, sr)

    words = transcription.split()
    word_durations = len(y) / sr / len(words)  # Average duration of each word
    occurrences = {}
    timestamps = []

    for keyword in keywords:
        occurrences[keyword] = {'count': 0, 'timestamps': []}
        for i, word in enumerate(words):
            if keyword.lower() in word.lower():
                occurrences[keyword]['count'] += 1
                timestamp = i * word_durations
                occurrences[keyword]['timestamps'].append(timestamp)
                timestamps.append(timestamp)

    print("Occurrences of given keyword:", occurrences)
    plot_keyword_occurrences(y, sr, timestamps)
    return occurrences, gender

# Plot keyword occurrences on the waveform graph
def plot_keyword_occurrences(y, sr, timestamps):
    plt.figure(figsize=(14, 5))
    librosa.display.waveshow(y, sr=sr, alpha=0.6)
    for timestamp in timestamps:
        plt.axvline(x=timestamp, color='r', linestyle='--', alpha=0.8)
    plt.title('Keyword Occurrences in Audio')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

# Example usage
audio_file_path = 'female3.wav'
keywords = ['yes']
occurrences, gender = keyword_spotting_and_gender_identification(audio_file_path, keywords)
print("Gender Identified:", gender)
