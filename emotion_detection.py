import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    data = { "raw_document": { "text": text_to_analyze } }

    if text_to_analyze.strip() != "":
        response = requests.post(URL, json=data, headers=HEADER)

        try:
            result = response.json()
            return result
        except Exception as e:
            print(repr(e), response.status_code, response.text)
    
    return { "error": "Please enter a valid text"}