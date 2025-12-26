import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP EmotionPredict service.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: Formatted dictionary with emotion scores and dominant emotion
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert response to dictionary
    response_dict = response.json()
    
    # Extract emotions from the response
    # Watson NLP response structure: response_dict['emotionPredictions'][0]['emotion']
    if 'emotionPredictions' in response_dict and len(response_dict['emotionPredictions']) > 0:
        emotions = response_dict['emotionPredictions'][0]['emotion']
    elif 'emotion' in response_dict:
        emotions = response_dict['emotion']
    else:
        # Fallback: return default values if structure is unexpected
        emotions = {}
    
    # Extract individual emotion scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find the dominant emotion (highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

