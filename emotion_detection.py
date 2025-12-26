import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP EmotionPredict service.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: The response from the emotion detection service containing the 'text' attribute
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
    
    # Return the response as a dictionary
    return response.json()