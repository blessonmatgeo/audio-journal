Audio Journal Dashboard with Sentiment Analysis


Overview
This project allows you to track your mood over time through journal entries using audio recordings. The app records audio, converts it to text, and analyzes the sentiment of each entry using TextBlob. The data is stored in a CSV file and displayed on a web-based dashboard. The dashboard provides insights into your mood trends and sentiment analytics.

Key Features:
- Audio Recording: Record audio entries, which are then transcribed into text.
- Sentiment Analysis: Each journal entry undergoes sentiment analysis to classify its mood (positive, negative, neutral).
- Dashboard: View journal entries along with their sentiment scores and corresponding emojis.
- Sentiment Analytics: Track the average sentiment over time and the counts of positive, neutral, and negative entries.



Technologies Used:
- Python 3.x: Backend programming language
- Flask: Web framework for creating the server-side application
- TextBlob: Library for sentiment analysis
- JavaScript: For handling dynamic content and interacting with the backend
- HTML & CSS: For building the user interface of the dashboard
- CSV: Storing journal entries and sentiment data
- Speech Recognition: To record and convert audio to text



How It Works:
- Audio Recording: The senti.py script allows you to record an audio journal entry for 15 seconds. The audio is converted to text, and sentiment analysis is performed to determine whether the entry is positive, negative, or neutral.
- Data Storage: The journal entry, sentiment score, and corresponding emoji are saved to a CSV file (journal_log.csv).
- Dashboard: The app.py script starts a web server using Flask. You can then access the web dashboard where you can view the journal entries along with their sentiment scores and emojis.
- Sentiment Analytics: The dashboard also provides sentiment analytics, including the average sentiment and the counts of positive, neutral, and negative entries.

Running the Application
- Step 1: Record Journal Entries (senti.py)
First, run the senti.py script to record audio journal entries. This script will:

Record audio for 15 seconds.
Convert the audio to text.
Perform sentiment analysis on the text.
Store the journal entry along with its sentiment data in the journal_log.csv file.
To run the script:

bash
Copy code
python senti.py
You can run this script multiple times to add more journal entries.

- Step 2: Start the Web Dashboard (app.py)
Once you have recorded some journal entries, you can start the Flask application (app.py) to view the entries on the dashboard and analyze the sentiment over time.

