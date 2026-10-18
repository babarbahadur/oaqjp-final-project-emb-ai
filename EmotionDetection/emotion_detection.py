import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=data, headers=HEADER)

    try:
        result = response.json()

        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
        all_emotions = result["emotionPredictions"][0]["emotion"]

        dominant_emotion = ''
        predicted_emotion_confidence = 0

        for emotion in all_emotions:
            if all_emotions[emotion] > predicted_emotion_confidence:
                predicted_emotion_confidence = all_emotions[emotion]
                dominant_emotion = emotion

        return {
            **all_emotions,
            "dominant_emotion": dominant_emotion
        }
    except Exception as e:
        print(repr(e), response.status_code, response.text)