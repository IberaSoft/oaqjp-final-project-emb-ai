"""
Flask web application for Emotion Detection
Deploys the EmotionDetection package as a web service
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Flask route to handle emotion detection requests
    Accepts GET parameter 'textToAnalyze' and returns formatted emotion analysis
    """
    # Get the text to analyze from the request
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)
    
    # Check if dominant_emotion is None (blank entry, status_code 400)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Format the response as specified
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formatted_response


@app.route("/")
def render_index_page():
    """
    Renders the main application page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
