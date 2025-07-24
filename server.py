''' Executing this function initiates the application of emotion detection to be executed over the
Flask channel and deployed on localhost:5000.'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and runs sentiment analysis over it using
    sentiment_analysis() function. The output returned shows the label and its confidence score for
    the provided text.'''
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_detection = emotion_detector(text_to_analyze)
    # Handle error when dominant_emotion is None
    if emotion_detection['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    result = "For the given statement, the system response is "
    result += f"'anger': {emotion_detection['anger']}, "
    result += f"'disgust': {emotion_detection['disgust']}, "
    result += f"'fear': {emotion_detection['fear']}, "
    result += f"'joy': {emotion_detection['joy']} and "
    result += f"'sadness': {emotion_detection['sadness']}. "
    result += f"The dominant_emotion is {emotion_detection['dominant_emotion']}."
    return result
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)


