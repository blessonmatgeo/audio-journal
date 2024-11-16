from flask import Flask, jsonify, send_from_directory
import csv
import datetime
from textblob import TextBlob
import os

app = Flask(__name__)

# Serve static files (HTML, CSS, JS)
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(os.getcwd(), path)

# Function to read journal entries from the CSV file
def read_journal_entries():
    entries = []
    try:
        with open('journal_log.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, text, mood, emoji = row
                sentiment = analyze_sentiment(text)
                entries.append({
                    'date': date,
                    'entry': text,
                    'mood': mood,
                    'emoji': emoji,
                    'sentiment': sentiment
                })
    except FileNotFoundError:
        print("CSV file not found.")
    return entries

# Function to analyze sentiment using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
    return sentiment

# Endpoint to get journal entries
@app.route('/api/journal', methods=['GET'])
def get_journal_entries():
    entries = read_journal_entries()
    return jsonify(entries)

# Endpoint to get sentiment analytics
@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    entries = read_journal_entries()
    sentiment_data = [entry['sentiment'] for entry in entries]

    if len(sentiment_data) > 0:
        avg_sentiment = sum(sentiment_data) / len(sentiment_data)
    else:
        avg_sentiment = 0.0
    
    positive_count = len([s for s in sentiment_data if s > 0])
    negative_count = len([s for s in sentiment_data if s < 0])
    neutral_count = len([s for s in sentiment_data if s == 0])

    analytics = {
        'avg_sentiment': avg_sentiment,
        'positive_count': positive_count,
        'negative_count': negative_count,
        'neutral_count': neutral_count
    }

    return jsonify(analytics)

if __name__ == '__main__':
    app.run(debug=True)

