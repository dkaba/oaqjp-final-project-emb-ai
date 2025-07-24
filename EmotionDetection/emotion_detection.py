import json
import  requests

def emotion_detector(text_to_analyze):
    '''This function send a post request to Watson NLP Library function passing it a text string to be analyse for emotion detection. It then
    process the response, extract, format and return the desired information '''
    #URL of the EMotion Predict function of the Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Initialize the result dictionary
    result = {}
    # Sending a POST request to the emotion Predict API
    response = requests.post(url, json=input_json, headers=header)
    # If the response status code is 400, return the same dictionary with values for all keys being None
    if response.status_code == 400:
        result = {"anger":None, "disgust":None, "fear":None, "joy":None, "sadness":None, "dominant_emotion":None}
        return result
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting emotions, including anger, disgust, fear, joy and sadness,along with their scores.
    emotion_prediction = formatted_response["emotionPredictions"][0]
    emotions = emotion_prediction["emotion"]
    result["anger"] = emotions["anger"]
    result["disgust"] = emotions["disgust"]
    result["fear"] = emotions["fear"]
    result["joy"] = emotions["joy"]
    result["sadness"] = emotions["sadness"]
    # Compute the highest score and get the linked emotion as the dominant emotion
    max_score = max(result.values())
    dominant_emotion = [emotion for emotion in result.keys() if result[emotion] >= max_score][0]
    result["dominant_emotion"] = dominant_emotion
    return result
