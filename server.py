"""
Flask web application for Emotion Detection.

This module deploys the EmotionDetection package as a web service,
providing a REST API endpoint for emotion analysis of text input.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests via GET method.

    This route accepts a 'textToAnalyze' parameter and returns formatted
    emotion analysis results. If the input is invalid (blank entry),
    returns an error message.

    Args:
        None (uses request.args.get('textToAnalyze'))

    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or error message "Invalid text! Please try again!" for blank entries.

    Example:
        GET /emotionDetector?textToAnalyze=I%20am%20happy
        Returns: "For the given statement, the system response is
                 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95
                 and 'sadness': 0.0. The dominant emotion is joy."
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
    Render the main application page.

    This route serves the HTML interface for the emotion detection
    application, allowing users to input text and view results.

    Returns:
        str: Rendered HTML template (index.html) containing the web interface.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
