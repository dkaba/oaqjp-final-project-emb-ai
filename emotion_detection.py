import json
import  requests
def emotion_detector(text_to_analyze):
    '''This function send a post request to Watson NLP Library function
    passing it a text string to be analyse for emotion detection. It then
    process the response, extract, format and return the desired information
    '''
    #URL of the EMotion Predict function of the Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion Predict API
    response = requests.post(url, json=input_json, headers=header)

    # Return the response as a text
    return response.text
