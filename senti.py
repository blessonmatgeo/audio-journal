import sounddevice as sd
import numpy as np
import wave
import csv
import datetime
import speech_recognition as sr
from textblob import TextBlob

# Record audio function using sounddevice
def record_audio(filename="journal.wav", duration=5):
    fs = 44100  # Sampling frequency
    print("Recording...")
    
    try:
        # Record the audio data
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")
        
        # Save the audio to a .wav file
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 2 bytes per sample (16-bit)
            wf.setframerate(fs)
            wf.writeframes(audio_data.tobytes())
        print(f"Audio saved to {filename}")
    
    except Exception as e:
        print(f"Error recording audio: {e}")

# Convert audio to text using SpeechRecognition
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    audio = None
    print(f"Transcribing audio from {audio_file}")
    
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        
        text = recognizer.recognize_google(audio)
        print(f"Transcribed text: {text}")
        return text
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

# Perform sentiment analysis and return emoji
def analyze_sentiment(text):
    print("Analyzing sentiment...")
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
    
    if sentiment > 0:
        mood = "Positive"
        emoji = "😊"
    elif sentiment < 0:
        mood = "Negative"
        emoji = "😞"
    else:
        mood = "Neutral"
        emoji = "😐"
    
    print(f"Sentiment: {mood} {emoji}")
    return mood, emoji, sentiment

# Log the text with timestamp and sentiment to CSV
def log_entry(text, mood, emoji):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("journal_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, text, mood, emoji])
        print(f"Entry logged: {timestamp}, {text}, {mood}, {emoji}")
    except Exception as e:
        print(f"Error logging entry: {e}")

# Main flow
def record_and_log_entry():
    print("Starting process...")
    record_audio("journal.wav", duration=5)  # Adjust duration as needed
    transcribed_text = audio_to_text("journal.wav")
    
    if transcribed_text:
        mood, emoji, sentiment = analyze_sentiment(transcribed_text)
        log_entry(transcribed_text, mood, emoji)
    else:
        print("No valid transcription received.")

# Run the flow
record_and_log_entry()
